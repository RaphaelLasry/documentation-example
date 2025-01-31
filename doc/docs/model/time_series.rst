:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Time Series
===========

.. contents::
    :depth: 2
    :local:


General introduction
--------------------

The concept of meters allows users to model more advanced constraints within the model, providing greater flexibility and precision. A meter's "raw" value acts as a counter, representing a weighted sum of model variables such as asset flows (e.g., production, consumption, buying, and selling), power capacities, and energy capacities.

This raw value is typically converted into a "read" value, which matches the raw value in most cases. However, if the meter only tracks positive values, any negative raw value will result in a read value of 0.

Users can apply constraints to each meter's "read" value, including minimum and maximum limits, or incorporate meter costs into the model's objective function. Additionally, meters can be organized hierarchically with parent (head) and child (sub) meters.

In summary, meters can be used to define joint constraints across assets or to regulate flows in/out of assets based on their respective power or energy capacities.

Technical description and model assumptions
-------------------------------------------

This section explains how Prosumer integrates meter objects into its model. It describes the parameters available and how it impacts the refinement of the behavior of the objects modelled.

.. admonition:: Prosumer's genericity
    :class: tip

    One of **Prosumer's main strengths is its versatility** in accommodating diverse scenario designs. **Meters further enhance this** by providing additional flexibility for the user. Such feature is quite powerful and can help to represent many situations. However, it is important to keep in mind that the more complex the model, the more challenging it can be to interpret the results (especially in the case of infeasible scenarios). Therefore, it is recommended to use meters judiciously and to document their use thoroughly.

Types of meters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prosumer distinguishes between two types of meters:

* **Positive meters** correspond to meters that only count positive values, meaning if their "read" value is the maximum between its "raw" value and 0.

* **Classic meters** correspond to meters that do not only count positive values, meaning their "read" value is equivalent to their "raw" value.

Note by default meters are considered as classic meters.

Assets flows and capacities contributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each meter has a raw value that corresponds to a weighted sum of asset flows, power capacities, and energy capacities. These categories are detailed below:

1) **Asset flows** :
Asset **flows are either the flows going "in" and "out"** of assets. Each asset flow can be weighted in some meter by coefficients :math:`\text{flow_in_weight}` and :math:`\text{flow_out_weight}`.

* For **assets derived from technologies** (e.g. Converter, Storage, Genset, RES, Station) or **markets**, the flows contribution can depend on the meter, asset (defined by a technology/market name and a node), type of flow (energy vector), the year and the time block.
* For **assets that are lines**, those depend on the meter, line name, the year and the time block (lines only have one flow type).

2) **Asset Power Capacity** :
Asset Power Capacity are the size in power capacity of assets. Each asset power capacity can be weighted in some meter by coefficients :math:`\text{power_weight}`.

* For **assets derived from technologies** (e.g. Converter, Storage, Genset, RES, Station) or **markets**, the power capacity contribution can depend on the meter, asset (defined by a technology/market name and a node) and the year.
* For **assets that are lines**, those depend on the meter, line name, the year.

3) **Asset Energy Capacity** :
Asset Energy Capacity are the size in energy capacity of assets that only apply to storage assets. Each storage asset energy capacity can be weighted in some meter by coefficients :math:`\text{energy_weight}`.

* For **storage assets**, the energy capacity contribution can depend on the meter, asset (defined by a technology name and a node) and the year.

.. admonition:: Warning
    :class: warning

    The user can only assign **energy capacity weight** different than 0 to some **storage asset** for any meter contribution.

Each meter's raw value is then converted in its read value and can be constrained by a minimum or maximum value, or even penalized by a cost.


.. raw:: html

   <details>
   <summary><a>Example - Click to Expand</a></summary>
   <div>

    For instance for some meter that has not not only positive count (read value equal to raw value), we can choose to force a \(\text{generator}\) asset to produce at most half its capacity (for some flow type, on some time block, defined for some years) using the following \(\text{meter}\) definition with minimal value of 0.


    We will then use \(\text{power_weight} = 0.5\) and \(\text{flow_out_weight} = -1\). This gives us the constraint :

        \begin{align*}

        \text{read_value}(\text{meter}) &= 0.5*\text{power_capacity}(\text{generator}) -1 *\text{flow_out}(\text{generator})\\
        0 &\le \text{read_value}(\text{meter})  \\
        \\
        \Leftrightarrow \text{flow_out}(\text{generator}) &\le 0.5*\text{power_capacity}(\text{generator})
        \end{align*}

    Of course you can have more advance constraints by combining multiple assets and flows on different years and time blocks in the meter definition.

   </div>
   </details>

    <div style="margin-top: 2em;"></div>

.. raw:: html

   <details>
   <summary><a>Mathematical summary of a meter</a></summary>
   <div>

    The concept of meters is quite generic and can be summarized mathematically as follows. Let's consider a meter \(\text{meter}\) with a raw value \(\text{raw_value}(\text{meter})\) that is a weighted sum of asset flows, power capacities, and energy capacities. The read value \(\text{read_value}(\text{meter})\) is then defined as :

        \begin{align*}
            \text{read_value}(\text{meter}) &= \sum_{\text{asset}} \sum_{\text{flow}} \sum_{\text{year}} \sum_{\text{time block}} \text{flow_weight}(\text{asset}, \text{flow}, \text{year}, \text{time block}) \times \text{flow}(\text{asset}, \text{flow}, \text{year}, \text{time block}) \\
            &+ \sum_{\text{asset}} \sum_{\text{year}} \text{power_weight}(\text{asset}, \text{year}) \times \text{power_capacity}(\text{asset}, \text{year}) \\
            &+ \sum_{\text{asset}} \sum_{\text{year}} \text{energy_weight}(\text{asset}, \text{year}) \times \text{energy_capacity}(\text{asset}, \text{year})
        \end{align*}

   </div>
   </details>

    <div style="margin-top: 2em;"></div>

Meters hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Prosumer, it is possible to define a hierarchy between meters. This means that a meter can be a head meter and have sub meters contributing to its value.

More concretely, if :math:`\text{head_meter}` is the head meter and has :math:`\text{sub_meter_}i` as its :math:`i^{\text{th}}` sub meter, then :math:`\text{head_meter}` raw value is given by :

.. math::

    \begin{align*}
    \text{raw_value}(\text{head_meter}) = \sum_{i} \;\; \text{sub_meter_weight_}i*\text{raw_value}(\text{sub_meter_}i)
    \end{align*}

where :math:`\text{sub_meter_weight_}i` is the weight of the :math:`i^{\text{th}}` sub meter associated to the head meter. Note there are hidden indices in this sum like :math:`\text{years}` and :math:`\text{time blocks}` that enable using only sub meter values for specific years and time blocks in the head meter contribution.

There is also a possibility to add a minimum and maximum share constraint in :math:`[\%]` for each sub meter contribution.


.. raw:: html

   <details>
   <summary><a>Example - Click to Expand</a></summary>
   <div>

    Assume all following meters are classic (not positive). For instance if two sub meters representing the quantity of \(\text{H}_2\) from source 1 and source 2 must add up to total \(\text{H}_2\) production representing head meter value, we can choose for example that first source is bounded between \(\text{min_share}=0\%\) and \(\text{max_share}=\alpha\%\), and source 2 between \(\text{min_share}=\beta\%\) and \(\text{max_share}=100\%\) of total \(\text{H}_2\) production. Which in mathematics states as:

        \begin{align*}
        \text{read_value}(\text{head_meter}) &= \text{read_value}(\text{sub_meter_source1}) + \text{read_value}(\text{sub_meter_source2}) \\
        0 &\le \text{read_value}(\text{sub_meter_source1}) \le \alpha/100*\text{read_value}(\text{head_meter})\\
        \beta/100*\text{read_value}(\text{head_meter}) &\le \text{read_value}(\text{sub_meter_source2}) \le 1
        \end{align*}

    Note there are also hidden indices in these constraints like \(\text{years}\) and \(\text{time blocks}\) that enable share constraints only for specific years and time blocks.

   </div>
   </details>

.. raw:: html

   <div style="margin-top: 2em;"></div>


Main Assumptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here are the main assumptions of meters :

* Any asset type can contribute to a meter, **except for assets of the "vehicle" type**, which are not considered in meters. Therefore, meters can be applied to converters, gensets, RES, storages, stations, and lines.
* Only **storage assets** have an energy capacity contribution, while all other assets contribute through power capacity and flow (in/out).
* Meter values can account for both **energy ([kWh]) and power ([kW]) contributions**, which means mathematically we will compare [kW] with [kWh].

.. admonition:: Note
    :class: note

    The energy and power capacity contributions can be mixed in a mathematical sense at any time block as those capacities are constant during the year.

