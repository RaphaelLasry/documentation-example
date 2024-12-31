:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

SDDP
====

.. contents::
    :depth: 2
    :local:

General introduction
--------------------

In Prosumer, users model scenarios that can be divided into different cases to incorporate variations. The objective of the global setup is to enable users to define the primary structure of the scenario and its key components. This includes defining cases, the optimization time horizon, flows (energy  vectors), scenario topology (nodes and distances), assets (technologies and markets), and pollutants.

This initial step in modeling provides an overview of the scenario and its main components, serving as a foundation for the more detailed modeling of the scenario in subsequent modules.

Technical description and model assumptions
-------------------------------------------

This section explains in more details each section of the global set up and its related assumptions.

.. admonition:: Prosumer's Global Set Up
    :class: tip

    Prosumer is a versatile tool with numerous features. The global setup **guides modelling** by providing a foundational framework.

Modeling Cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each Prosumer's scenario contains at least one case, the base case. The user can define additional cases to optimize different scenario variations of the base case, which might save modeling time instead of modeling a new scenario from scratch for each variation.

For each case, the user can choose the following parameters :

* **Optimization criteria** which goes between "NPV" (optimizing Net Present Value) and "CO2" (minimizing CO2 emissions).
* **Discount rate** (also known as WACC for weighted average cost of capital) which is used to calculate the Net Present Value.
* The **maximum discounted total cost** in [EUR] which is used to constraint the total cost of the scenario.

Note all other features are depreciated and will be removed in future versions.

.. admonition:: Case Variations
    :class: note

    Although we can assign different case parameters as explained previously, even **more differences between cases can be done in next modeling steps** by modifying the case related technologies, markets, lines, pollutants, meters and much more.

Time Horizon, Time Intervals and Time Partition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1) **Time Horizon**

In Prosumer, the optimization occurs over a **time horizon (in years)**, which must be the same for all cases. On that time horizon, we optimize the **investment decisions (asset sizing)** for all years. However, the user must also define optimization years which will be a subset of the year span where only the optimization of the **operational decisions (dispatch)** will be done. The choice of not optimizing dispatch on each year can be useful for data or computational time purposes.

One simple example for the user would be to optimize from 2025 to 2050, but only optimize dispatch for 2025, 2035, 2045 if the user feels like those three years represent well the entire year span of the scenario.

2) **Time Intervals**

In Prosumer, **granularity for optimization is set to hours**. For each case, the years to optimize are by default divided into 8760 hours (365 days * 24 hours). However, the user can choose to only consider subsets of those 8760 hours by defining **hour intervals**. Those intervals can be different between any case and optimized year pair. This feature can **reduce drastically the size of the problem** in order to quickly obtain good approximate decisions. Be aware that the selection of the period should be done carefully. If non-representative periods are provided, poor sizing decisions might be given by Prosumer.

For instance, the user can feel the first 1000 hours of the years are representative of the entire year and decide to optimize only on those hours (for all cases and years to optimize). This will drastically reduce the size of the problem.

3) **Time Partition**

In Prosumer, the user can also model time partitions, where one time partition corresponds to **assigning some time blocks (labels) to each of 8760 hours**. Note by default the time partition is called "default_yearly_tp" with only one time block "default_yearly_tb", meaning all hours are labeled the same and we consider only one big time block corresponding to the entire year.

The user could for instance label all hours in 7 time blocks : "Mondays_hours" up to "Sunday_hours". This would enable the user to model constraints on certain specific days of the week. Of course there is no limit to the number of time partitions and time blocks that can be defined.

.. admonition:: Warning
    :class: warning

    Pay attention that each time block name should be related to a single time partition.


Flows
^^^^^^^^^^^^^^^^^^^^^

In Prosumer, flows are **energy vectors** that are considered in the model. Those flows can be produced by assets or bought from retail markets, they can be converted into other flows using converter assets, and finally they can be consumed by demand or sold on wholesale markets.
The user can define all the flows he wants to consider in the scenario.

.. admonition:: Prosumer's multi-dimensionality
    :class: tip

    Prosumer is a generic tool with **multiple dimensions**. One main dimension represents **flows that evolve in two other dimensions which are time and location**. Flows can be produced, converted, consumed, bought and sold at any defined time on any defined node.


Technologies and Markets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Prosumer, the user can define the technologies and markets that will be considered in the scenario, where he can stipulate their **types**, **location (which node)** and whether they are **virtual assets** or not (meaning they have no impact on the Total Cost of Ownership). By default all assets are **not virtual assets**. Introducing virtual assets can be relevant for modelisation purpose.

Here is the list of all different types of technologies/markets :

* **Converter** : A technology that can convert flows into other flows. For instance, a heat pump converting electricity into heat.
* **VRES** : Variable renewable energy sources, that can be divided into **Solar** and **Wind** in Prosumer. For instance, solar panels or wind turbines.
* **Storage** : A technology that can store flows. For instance, batteries storing electricity.
* **Genset** : A generator technology that can produce flows based on some input flow. For instance, a diesel generator producing electricity.
* **Vehicle** : A vehicle technology that is constrained to drive a certain distance. For instance, an electric vehicle. Note the node name on which it is defined is not a classic node (geographic) but the name of the fleet to which it corresponds. See **Mobility section**.
* **Connector** : A station that can connect vehicle technologies to the grid. For instance, a charging station.
* **Market** : A market where flows can be bought (retail) or sold (wholesale). For instance, a retail electricity market.


.. admonition:: Base case heritage
    :class: important

    In Prosumer's modelling logic, if we define an object/parameter on the base case, it **applies to all other cases** unless explicitly stipulated. Note it is **applicable on the User Interface**, where defining any technology/market on the basecase will automatically define it on all cases. However, in the Excel template (more advance usage), the user must define for each case the technologies/markets he wants to consider. There is **no base case heritage in the Excel template** regarding the technologies/markets definition.

.. admonition:: Definition of technology/market asset
    :class: note

    Note any **technology/market asset** is defined based on its **techno/market name**, and on the **node** it is defined on. Two technologies with the same name on different nodes are considered as different assets. However, some technological asset (e.g. converters) can have multiple flows going in and out, and thus **assigning different flows does not make them different assets**.


Node and distances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Prosumer, we can define a **model topology** where we can define **nodes and distances** between them. Nodes are the locations where assets are defined and where flows are exchanged. Distances are the distances between nodes, which can be used to model constraints on the flows between nodes. This enables the **modelling of a network** where flows are produced/consumed/bought/sold on some nodes and can be **transported though lines between node pairs**, see section dedicated to **Lines assets**.

By default, there is only one node in the problem and all assets are defined on that node.

Pollutants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Prosumer, the user can define pollutants that will be considered in the scenario. Pollutants can be emitted by assets and those **emissions can be constrained** and **penalized** in the model. We can define the following parameters :

* **Scope Weights** : those weights (three for each scope 1, 2 and 3) are used to penalize in each scope the emissions. Those weights depend on the case, pollutant and can also depend on the node.
* **Maximum Total Emissions** : the maximum total emissions of the pollutant in [kg] corresponds to the upper bound of total emissions for any case, pollutant and node if desired.

.. admonition:: CO2 default pollutant
    :class: note

    **CO2** is always defined as **default pollutant** in Prosumer, but the user can add any other pollutant he wants to consider in the scenario.




Excel input sheets
------------------



.. admonition:: 1 Global - Cases
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ is solved?
        * *Description:* Binary flag indicating if the case should be solved (1) or not (0).
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ optimization criteria
        * *Description:* What do you aim to optimize? 2 choices: 'NPV' (Net Present Value) or 'CO2' emissions.
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ discount rate
        * *Description:* Discount rate used to calculate the Net Present Value (NPV), also known as WACC (Weighted Average Cost of Capital). Expressed in % between 0.0 and 100.0
        * *Default value:* (TBD)
        * *Default unit:* %
        * *Validity:* (TBD)
    ⚙️ inflation rate
        * *Description:* Depreciated
        * *Default value:* (TBD)
        * *Default unit:* %
        * *Validity:* (TBD)
    ⚙️ tax (depreciation)
        * *Description:* Depreciated
        * *Default value:* (TBD)
        * *Default unit:* %
        * *Validity:* (TBD)
    ⚙️ tax (revenue)
        * *Description:* Depreciated
        * *Default value:* (TBD)
        * *Default unit:* %
        * *Validity:* (TBD)
    ⚙️ max discounted total cost
        * *Description:* Maximum (discounted) total cost for the case in [EUR], representing CAPEX + OPEX over all years discounted by the WACC or discount factor. In case of any constraint, enter a non negative value, otherwise leave it empty.
        * *Default value:* (TBD)
        * *Default unit:* EUR
        * *Validity:* (TBD)


.. admonition:: 1 Global - Time frame
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)



.. admonition:: 1 Global - Repr time interval
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ weight
        * *Description:* Weight (magnitude of importance) given to the selected time interval, between 0.0 and 1.0. The sum of all weights for a given optimized year should be equal to 1.0
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)


.. admonition:: 1 Global - Flow
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)



.. admonition:: 1 Global - Nodes
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ node area
        * *Description:* Surface area of the node in [m^2]. In case of any constraint, enter a positive value, otherwise leave it empty.
        * *Default value:* (TBD)
        * *Default unit:* m^2
        * *Validity:* (TBD)
    ⚙️ maximum noise intensity level
        * *Description:* Maximum total noise intensity level for the assets of the node in [kW/m^2]. It is possible to define a noise power parameter for the different technologies and a distance to the measurement point on the node (at which the noise constraint should be verified). In fact, the noise intensity is a function of the distance to the measurement point. In case of any constraint, enter a positive value, otherwise leave it empty.
        * *Default value:* (TBD)
        * *Default unit:* kW/m^2
        * *Validity:* (TBD)


.. admonition:: 1 Global - Nodes distances
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ distance
        * *Description:* Distance between origin and destination nodes expressed in [m]. This distance is used to calculate the line length from any origin to any destination node. In case of any line defined in the scenario, enter a positive value, otherwise leave it empty.
        * *Default value:* (TBD)
        * *Default unit:* m
        * *Validity:* (TBD)


.. admonition:: 1 Global - Technologies Markets
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ is virtual?
        * *Description:* Is this asset virtual, i.e. having no impact on the TCO and added for modelisation purposes only (no physical reality)? If yes, enter 1. If no, enter 0. A virtual asset wont appear or will be flagged as such on some output sheets.
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)


.. admonition:: 1 Global - Pollutants
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ max total emission
        * *Description:* Maximum total (discounted) pollutant emission for the case over all years, expressed in [kg] of according pollutant. In case of any constraint, enter a non negative value, otherwise leave it empty.
        * *Default value:* (TBD)
        * *Default unit:* kg
        * *Validity:* (TBD)
    ⚙️ pollutant_scope_global_weights
        * *Description:* (TBD)
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ weight - scope1
        * *Description:* (TBD)
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ weight - scope2
        * *Description:* (TBD)
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ weight - scope3
        * *Description:* (TBD)
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ emissions actualisation factor
        * *Description:* Discount factor for pollutant emissions. If a discount applies, enter a non-negative value. Otherwise, leave the cell empty to apply no discount by default.
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)


.. admonition:: 1 Global - Pollutants Nodal
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

    ⚙️ pollutant_scope_weights
        * *Description:* (TBD)
        * *Default value:* (TBD)
        * *Default unit:* (TBD)
        * *Validity:* (TBD)
    ⚙️ max total nodal emission
        * *Description:* Maximum total (discounted) pollutant emissions of pollutant for the node, expressed in [mass unit]. In case of any constraint, enter a non negative value, otherwise leave it empty.
        * *Default value:* (TBD)
        * *Default unit:* mass unit
        * *Validity:* (TBD)


.. admonition:: 1 Global - Time partition
    :class: note

    *Sheet description*: (TBD)

    *Mandatory sheet*: (TBD)

