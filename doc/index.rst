:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Cactus user documentation
===========================

AAAA The purpose of this document is to provide a comprehensive guide on how to use the Cactus software. You will find both a general modeling guidelines for Cactus's modules and detailed parameter documentation for all input sheets. 

Cactus in a nutshell
----------------------

Cactus helps you optimize the dispatch of the gas in the world and operate the storages in order to get a view on the mid term market evolution.

.. admonition:: Cactus purpose and model
    :class: tip

    **Cactus provides the optimal dispatch of your energy system minimizing its Total Cost of Ownership (TCO).**

    The tool is based on a *linear programming (LP)* model that optimizes the operation of a set of assets (appros, storages, pipes, markets etc.) and their interconnections (PIR, PTS, PTM) to meet a set of energy demands. The optimization problem is defined as follows [#capacity_energy]_:

    .. math::

        \begin{align*}
                \min \quad& \text{Cost production} \\
                &+ \text{Cost transport} \\
                &+ \text{Cost storage} \\
                &+ \text{Cost of markets} \\
                &+ \text{Cost of regasification} \\
                &+ \text{Cost of liquefaction} \\
                \text{if LNG:} \quad&+ \text{Cost of shipping} \\
                \text{if SDDP:} \quad&+ \text{Cost of future objective} \\
                \text{if Ecart:} \quad&+ \text{Cost of imbalance} \\[3ex]
                \text{subject to} \quad& \text{Balance constraints} \quad \textit{ (flow conservation)} \\
                & \text{Operating constraints} \quad \textit{ (technical limitations, design requirements or choices)} \\
                & \text{Ambition constraints} \quad \textit{ (emissions, RES share)} \\
                & \text{Capacity constraints} \quad \textit{ (transport, storage, production)} \\
                & \text{Market constraints} \quad \textit{ (transaction limits, prices)} \\
                & \text{Maintenance constraints} \quad \textit{ (periodic maintenance schedules)} \\
                & \text{...}
        \end{align*}

.. The focus of the tool is on strategic assessment of distributed energy projects , i.e. **pre-feasibility studies**. The tool plans, at different territory levels (industrial parks, campuses, eco-districts, regions), the optimal sizing and dispatching of all physical assets and provides key indicators of the resulting techno-economic performance (return on investment, levelized cost of energy, etc.), environmental footprint/avoided emissions, etc.

.. The tool is available for all ENGIE entities via a yearly license fee. A one-month free trial is available.

.. [#capacity_energy] Mosts of the costs that are both for the flow (MWh) and the capacity (MW) of the asset. It is possible in Cactus to add part of the existing capacity for different type of objects.

.. toctree::
    :caption: Module's documentation
    :maxdepth: 2
    :numbered: 1
    :hidden:

    docs/global_parameters
    docs/demand
    docs/production
    docs/market
    docs/lng
    docs/pipeline
    docs/storage
    docs/sddp
    docs/shipping
    docs/time_series

