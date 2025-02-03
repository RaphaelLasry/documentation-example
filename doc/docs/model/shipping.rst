:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Shipping
========

.. contents::
    :depth: 2
    :local:


Excel input sheets
------------------

.. _target_lng_nodes:
.. admonition:: LNGNodes
    :class: error

    *Sheet Description*: The notion of LNG Nodes differs from the concept of zones. Here a LNG Nodes should be seen as a physical location where LNG can be loaded or unloaded. The LNG Nodes are defined by the user and can be used to define the shipping routes between them.

    .. list-table::
        :widths: 25 25
        :header-rows: 1

        * - Nodes	
          - Max nb vessels
        * - Nodes (eg: LNG_AE)
          - Maximum number of vessels (eg: 37)

    *Mandatory sheet*: ❌

.. _lng_nodes:

    ⚙️ Nodes
        * *Description*: Name of the LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String.

    ⚙️ Max nb vessels
        * *Description*: Maximum number of vessels that can be loaded or unloaded at the node.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer

.. _target_shipping_dist:
.. admonition:: ShippingDist
    :class: error

    *Sheet Description*: This sheet defines the distance between the origin and destination LNG nodes in nautical miles.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Origin	
          - Destination
          - Distance [nm]
        * - Origin (eg: LNG_AE)
          - Destination (eg: LNG_AO)
          - Distance in nautical miles (eg: 6555)

    *Mandatory sheet*: ❌

.. _shipping_dist:

    ⚙️ Origin
        * *Description*: Name of the origin LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Destination
        * *Description*: Name of the destination LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Distance [nm]
        * *Description*: Distance between the origin and destination in nautical miles. 1 nautical miles is equal to 1.852 km.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer

.. _target_vessels:
.. admonition:: Vessels
    :class: error

    *Sheet Description*: This sheet defines the characteristics of the vessels that can be used to transport LNG between the LNG nodes.

    .. list-table::
        :widths: 25 25 25 25 25 25 25
        :header-rows: 1

        * - Type	
          - Capacity hold [MWh]	
          - Speed [kn]	
          - BOR [%]	
          - Charter cost [€/MWh of Capacity/day]	
          - Average cargo size [MWh]	
          - Initial Laden Share
        * - Type (eg: ARC7)
          - Capacity of the hold in MWh (eg: 17,514,435)
          - Speed in knots (eg: 16)
          - Boil off rate in % (eg: 0.12%)
          - Charter cost in €/MWh of capacity per day (eg: 0)
          - Average cargo size in MWh (eg: 1,144,913)
          - Initial laden share in % (eg: 60%)

    *Mandatory sheet*: ❌

.. _vessels:

    ⚙️ Type
        * *Description*: Name of the vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String.

    ⚙️ Capacity hold [MWh]
        * *Description*: Capacity of the hold in MWh.
        * *Default value*: 0
        * *Default unit*: MWh
        * *Validity*: Float

    ⚙️ Speed [kn]
        * *Description*: Speed of the vessel in knots. One knot is equal to 1.852 km/h.
        * *Default value*: 0
        * *Default unit*: knots
        * *Validity*: Float

    ⚙️ BOR [%]
        * *Description*: Boil off rate in %.
        * *Default value*: 0
        * *Default unit*: %
        * *Validity*: Float

    ⚙️ Charter cost [€/MWh of Capacity/day]
        * *Description*: Charter cost in €/MWh of capacity per day.
        * *Default value*: 0
        * *Default unit*: €/MWh of capacity per day
        * *Validity*: Float

    ⚙️ Average cargo size [MWh]
        * *Description*: Average cargo size in MWh.
        * *Default value*: 0
        * *Default unit*: MWh
        * *Validity*: Float

    ⚙️ Initial Laden Share
        * *Description*: Initial laden share in %.
        * *Default value*: 0
        * *Default unit*: %
        * *Validity*: Float

.. _target_lng_nodes_accept:
.. admonition:: LNGNodesAccept
    :class: error

    *Sheet Description*: This sheet defines the acceptance of the LNG nodes to import and export LNG.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Nodes	
          - Type
          - Accept import
          - Accept export
        * - Nodes (eg: LNG_AE)
          - Type (eg: Q-Flex)
          - Accept import (eg: 1)
          - Accept export (eg: 0)

    *Mandatory sheet*: ❌

.. _lng_nodes_accept:

    ⚙️ Nodes
        * *Description*: Name of the LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Type
        * *Description*: Name of the vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the types defined in the :ref:`Vessels<target_vessels>` sheet.

    ⚙️ Accept import
        * *Description*: 1 if the node can accept import, 0 otherwise.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer

    ⚙️ Accept export
        * *Description*: 1 if the node can accept export, 0 otherwise.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer

.. _target_vessels_restrictions:
.. admonition:: VesselsRestrictions
    :class: error

    *Sheet Description*: This sheet defines the acceptance of the vessels to follow a specific route.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Origin	
          - Destination	
          - Type	
          - Accept
        * - Origin (eg: LNG_BELUX)
          - Destination (eg: LNG_RU-Urals)
          - Type (eg: ARC7)
          - Accept (eg: 1)

    *Mandatory sheet*: ❌

.. _vessels_restrictions:

    ⚙️ Origin
        * *Description*: Name of the origin LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Destination
        * *Description*: Name of the destination LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Type
        * *Description*: Name of the vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the types defined in the :ref:`Vessels<target_vessels>` sheet.

    ⚙️ Accept
        * *Description*: 1 if the vessel can accept the route, 0 otherwise.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer

.. _target_addit_shipping:
.. admonition:: AdditShipping
    :class: error

    *Sheet Description*: This sheet defines the additional shipping capacity for each vessel type and LNG node.

    .. list-table::
        :widths: 25 25 25 25 25
        :header-rows: 1

        * - Vessel type	
          - LNG node		
          - Period1	
          - Period2
          - ...
        * - Vessel type (eg: ARC7)
          - LNG node (eg: LNG_RU-Urals)
          - 01/01/2020 (eg: 0)
          - 02/02/2020 (eg: 1 200 000)
          - ...

    *Mandatory sheet*: ❌

.. _addit_shipping:

    ⚙️ Vessel type
        * *Description*: Name of the vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the types defined in the :ref:`Vessels<target_vessels>` sheet.

    ⚙️ LNG node
        * *Description*: Name of the LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Period1, Period2, ...
        * *Description*: Additional shipping capacity for each period. The capacity is in MWh/day.
        * *Default value*: 0
        * *Default unit*: MWh/day
        * *Validity*: Float. The periods must be defined in the :ref:`Horizon<target_periods>` sheet.

.. _target_canal_cost:
.. admonition:: CanalCost
    :class: error

    *Sheet Description*: This sheet defines the cost of the canal for each vessel type and LNG node.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - LNG node
          - Vessel type	
          - Cost laden [€/MWh of Capacity]	
          - Cost ballast [€/MWh of Capacity]
        * - LNG node (eg: LNG_Panama)
          - Vessel type (eg: ARC7)
          - Cost laden in €/MWh of capacity (eg: 0.32)
          - Cost ballast in €/MWh of capacity (eg: 0.29)

    *Mandatory sheet*: ❌

.. _canal_cost:

    ⚙️ LNG node
        * *Description*: Name of the LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Vessel type
        * *Description*: Name of the vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the types defined in the :ref:`Vessels<target_vessels>` sheet.

    ⚙️ Cost laden [€/MWh of Capacity]
        * *Description*: Cost in €/MWh of capacity when the vessel is laden.
        * *Default value*: 0
        * *Default unit*: €/MWh of capacity
        * *Validity*: Float

    ⚙️ Cost ballast [€/MWh of Capacity]
        * *Description*: Cost in €/MWh of capacity when the vessel is in ballast.
        * *Default value*: 0
        * *Default unit*: €/MWh of capacity
        * *Validity*: Float

.. _target_transit_capacity:
.. admonition:: TransitCapacity
    :class: error

    *Sheet Description*: This sheet defines the maximum number of vessels that can transit each LNG node in each period.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - LNG node    
          - Period1
          - Period2
          - ...
        * - LNG node (eg: LNG_Panama)
          - 01/01/2020 (eg: 2)
          - 02/02/2020 (eg: 4)
          - ...

    *Mandatory sheet*: ❌

.. _transit_capacity:

    ⚙️ LNG node
        * *Description*: Name of the LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Period1, Period2, ...
        * *Description*: Maximum number of vessels that can transit the node in each period.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer. The periods must be defined in the :ref:`Horizon<target_periods>` sheet.

.. _target_route_unavailable:
.. admonition:: RouteUnavailable
    :class: error

    *Sheet Description*: This sheet defines the routes that are unavailable between the origin and destination LNG nodes in each period.

    .. list-table::
        :widths: 25 25 25 25 25
        :header-rows: 1

        * - Origin	
          - Destination	
          - Period1	
          - Period2
          - ...
        * - Origin (eg: LNG_RU-Urals)
          - Destination (eg: LNG_CN)
          - 01/01/2020 (eg: 1)
          - 02/02/2020 (eg: 0)
          - ...

    *Mandatory sheet*: ❌

.. _route_unavailable:

    ⚙️ Origin
        * *Description*: Name of the origin LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Destination
        * *Description*: Name of the destination LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Period1, Period2, ...
        * *Description*: 1 if the route is unavailable, 0 otherwise.
        * *Default value*: 0
        * *Default unit*: *None*
        * *Validity*: Integer. The periods must be defined in the :ref:`Horizon<target_periods>` sheet.

.. _target_transhipment:
.. admonition:: Transhipment
    :class: error

    *Sheet Description*: This sheet defines the transhipment costs between the source and destination vessel types at each LNG node.

    .. list-table::
        :widths: 25 25 25 25 25
        :header-rows: 1

        * - LNG node	
          - Source Vessel Type
          - Destination Vessel Type	
          - Unit cost [€/MWh]	
          - BOR
        * - LNG node (eg: LNG_BELUX)
          - Source Vessel Type (eg: ARC7)
          - Destination Vessel Type (eg: ARC4)
          - Unit cost in €/MWh (eg: 0.2)
          - Boil off rate in % (eg: 0.5)

    *Mandatory sheet*: ❌

.. _transhipment:

    ⚙️ LNG node
        * *Description*: Name of the LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Source Vessel Type
        * *Description*: Name of the source vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the types defined in the :ref:`Vessels<target_vessels>` sheet.

    ⚙️ Destination Vessel Type
        * *Description*: Name of the destination vessel type.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the types defined in the :ref:`Vessels<target_vessels>` sheet.

    ⚙️ Unit cost [€/MWh]
        * *Description*: Unit cost in €/MWh.
        * *Default value*: 0
        * *Default unit*: €/MWh
        * *Validity*: Float

    ⚙️ BOR
        * *Description*: Boil off rate in %.
        * *Default value*: 0
        * *Default unit*: %
        * *Validity*: Float

.. _target_lng_contracts:
.. admonition:: LNGContracts
    :class: error

    *Sheet Description*: This sheet defines the contracts between the origin and destination LNG nodes. The contract model a quantity of gas that must transit from one node to another.

    .. list-table::
        :widths: 25 25 25 25 25 25
        :header-rows: 1

        * - Contract	
          - PeriodeDebut	
          - PeriodeFin	
          - ACQ	
          - DCQ min	
          - DCQ max
        * - Contract (eg: LNG_DZ>FR)
          - Start period (eg: 01/01/2014)
          - End period (eg: 01/01/2023)
          - Annual Contract Quantity (eg: 36,570,000)
          - Minimum DCQ (eg: DCQmin_LNG_DZ>FR)
          - Maximum DCQ (eg: 1,500,000)

    *Mandatory sheet*: ❌

.. _lng_contracts:

    ⚙️ Contract
        * *Description*: Name of the contract.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String.

    ⚙️ PeriodeDebut
        * *Description*: Start period of the contract.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: Date.

    ⚙️ PeriodeFin
        * *Description*: End period of the contract.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: Date.

    ⚙️ ACQ
        * *Description*: Annual Contract Quantity in MWh.
        * *Default value*: 0
        * *Default unit*: MWh
        * *Validity*: Float or String. If String, then it must refer to a value defined in the :ref:`ACQParDate<target_acq_par_date>` sheet. 

    ⚙️ DCQ min
        * *Description*: Minimum Daily Contract Quantity in MWh/day.
        * *Default value*: 0
        * *Default unit*: MWh/day
        * *Validity*: Float or String. If String, then it must refer to a value defined in the :ref:`DCQParPdt<target_dcq_par_pdt>` sheet.

    ⚙️ DCQ max
        * *Description*: Maximum Daily Contract Quantity in MWh/day.
        * *Default value*: 0
        * *Default unit*: MWh/day
        * *Validity*: Float or String. If String, then it must refer to a value defined in the :ref:`DCQParPdt<target_dcq_par_pdt>` sheet.

.. _target_contract_routes:
.. admonition:: ContractRoutes
    :class: error

    *Sheet Description*: This sheet defines the routes between the origin and destination LNG nodes for each contract.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Contract	
          - Origin	
          - Destination	
        * - Contract (eg: LNG_DZ>FR)
          - Origin (eg: LNG_DZ)
          - Destination (eg: LNG_FR)

    *Mandatory sheet*: ❌

.. _contract_routes:

    ⚙️ Contract
        * *Description*: Name of the contract.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the contracts defined in the :ref:`LNGContracts<target_lng_contracts>` sheet.

    ⚙️ Origin
        * *Description*: Name of the origin LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.

    ⚙️ Destination
        * *Description*: Name of the destination LNG node.
        * *Default value*: *None*
        * *Default unit*: *None*
        * *Validity*: String. Must be part of the nodes defined in the :ref:`LNGNodes<target_lng_nodes>` sheet.