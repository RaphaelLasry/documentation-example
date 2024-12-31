:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Cactus user documentation
===========================

The purpose of this document is to provide a comprehensive guide on how to use the Cactus software. You will find both a general modeling guidelines for Cactus's modules and detailed parameter documentation for all input sheets. 

Cactus in a nutshell
----------------------

Cactus helps you optimize the dispatch of the gas in the world and operate the storages in order to get a view on the mid term market evolution.

.. admonition:: Cactus purpose and model
    :class: tip

    **Cactus provides the optimal dispatch of your energy system minimizing its Total Cost of Ownership (TCO).**

    The tool is based on a *linear programming (LP)* model that optimizes the operation of a set of assets (appros, storages, pipes, markets etc.) and their interconnections (PIR, PTS, PTM) to meet a set of energy demands. The optimization problem is defined as follows [#capacity_energy]_:

    .. math::

        \begin{align*}
                \min \quad& \text{Gas production and supply costs} \\
                &+ \text{Storage costs} \\
                &+ \text{Tariffs and costs for entry and exit points} \\
                &+ \text{Additional capacity} \\
                \text{if LNG:} \quad&+ \text{Shipping costs} \\
                \text{if SDDP:} \quad&+ \text{Cost of future objective} \\
                \text{if Ecart:} \quad&+ \text{Penalties and imbalances} \\[3ex]
                \text{subject to} \quad& \text{Balance constraints} \quad \textit{ (flow conservation)} \\
                & \text{Operating constraints} \quad \textit{ (minimum/maximum offtake for contracts)} \\
                & \text{Storage level} \quad \textit{ (CATS and tunnel)} \\
                & \text{Shipping capacity} \quad \textit{ (load and unload on vessels)} \\
                & \text{Maintenance constraints} \quad \textit{ (periodic maintenance schedules)} \\
                & \text{...}
        \end{align*}

.. [#capacity_energy] Mosts of the costs that are both for the flow (MWh) and the capacity (MW) of the asset. It is possible in Cactus to increase part of the existing capacity for different type of objects.

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

