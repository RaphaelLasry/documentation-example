:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

.. role:: underline
    :class: underline

Demand
======

.. contents::
    :depth: 2
    :local:

General introduction
--------------------

The demand module is used to define the load of each region. The demand is defined by zones and can be of different types. It can be defined in three different sheets, which correspond to different constraints added to the model:

     - `DemandeNormale`: it correspond to the load that :underline:`must` be satisfy by the system,
     - `DemandeInter`: it correspond to the load that :underline:`could` be met. Indeed, here there is a tradeoff between meeting the demand of paying the fee to not meet the requirement,
     - `DemandeTransit`: it allows the user to shift a demand from one PIR to another. **This module is depreciated and the model is not instantiated by this sheet.**

Technical description and model assumptions
-------------------------------------------

The demand that is passed by the user on the sheet `DemandeNormale` is read by the pre-processing script, transformed into a GAMS parameter called `ClientNormalDemande` and is then summed over the zone to create the parameter `Demande(z, p)`. The meeting of the demand is presented in the model as a balance equation between the inflows and outflows at a given nodal zone. Here is a simple representation of the balance equation for a given zone `z` and a given period `p`:


**Zone Balance Equation**

This equation ensures that the total inflow and outflow of resources in a zone are balanced. Here's a breakdown of the main components:

1. **Inflow Components:**
     - **PIR, PITS, PTM, Marche, and Liaison Aval:** These terms represent the quantities entering the zone from various sources like PIR, PITS, PTM, Marche, and Liaison Aval.

.. math:: \text{Inflow} = \sum (\text{PIR}) + \sum (\text{PITS}) + \sum (\text{PTM}) + \sum (\text{Marche}) + \sum (\text{Liaison Aval})

2. **Outflow Components:**
     - **PIR, PITS:** Quantities exiting the zone.
     - **Demand:** The demand in the zone, including technical consumption.
     - **Technical Consumption in Regas Plants (PTM, TM, Liaison):** Adjustments for fuel used in regasification plants.
     - **Demand Inter:** Additional demand in the zone ...
     - **Effacement:** ... That could be shut down partially.
     - **Technical Consumption in Pipes:** Fuel used in pipelines, split between upstream and downstream zones.
     - **PITL:** Quantities used for the liquefaction plants.

.. math:: \text{Outflow} = \sum (\text{PIR}) + \sum (\text{PITS}) + \text{Demand} + \text{Technical Consumption} + \text{Demand Inter} - \text{Effacement} + \sum (\text{Pipes}) + \text{PITL}

3. **Slack:**
     - **EcartActif:** Slacks based on active discrepancies in demand.

.. math:: \text{Adjustment} = \text{EcartActif} \times (\text{eZonePlus} - \text{eZoneMoins}) \times (\text{Demand} > 0)

**Overall Balance Equation:**

.. math::
    Inflow = Outflow + Slacks

For a more detailed view, the user can look at the equation `CtrBilanZone(z,p)` in the ModeleGAMS.gms file.

Excel input sheets
------------------

.. _target_demand_normale:
.. admonition:: DemandeNormale
    :class: error

    *Sheet description*: This sheet controls the global **daily** demand by zone on each time period. This sheet is dynamic in a sense that you must add the periods define in your use case as columns.

    .. list-table::
        :widths: 25 25 25 25 25
        :header-rows: 1

        * - Nom
          - Zone
          - Periode1
          - Periode2
          - ...
        * - DemandName1
          - ZoneName1
          - Value11
          - Value21
          - ...
        * - DemandName2
          - ZoneName2
          - Value12
          - Value22
          - ...

    *Mandatory sheet*: ❌

.. _demand_normale:

    ⚙️ Nom
        * *Description:* Unique name of the demand. It could be also the same name of the zone.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Zone
        * *Description:* Name of a zone.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the zones defined in the :ref:`Zones<target_zones>` sheet.

    ⚙️ Periode1, Periode2, ...
        * *Description:* Demand value for each period. Warning, this demand is in MWh/day and will be multiplied by the number of days in the period.
        * *Default value:* 0
        * *Default unit:* MWh/day
        * *Validity:* Float. The periods must be defined in the :ref:`Horizon<target_periods>` sheet.

.. _target_demand_inter:
.. admonition:: DemandeInter
    :class: error

    *Sheet description*: This sheet controls the global **daily** interruptive demand by zone on each time period. This sheet is dynamic in a sense that you must add the periods define in your use case as columns.

    .. list-table::
        :widths: 25 25 25 25 25 25
        :header-rows: 1

        * - Entete
          - Nom
          - Zone
          - Periode1
          - Periode2
          - ...
        * - Flag1
          - DemandName1
          - NomZone1
          - Value11
          - Value21
          - ...
        * - Flag2
          - DemandName2
          - NomZone2
          - Value12
          - Value22
          - ...

    *Mandatory sheet*: ❌

.. _demand_inter:

    ⚙️ Entete
        * *Description:* String to define the nature of the series. It must be part of the list:
            * Demande Inter
            * Prix Inter Optim
            * Prix Inter Reel
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Nom
        * *Description:* Unique name of the demand. The couple (Entete, Nom) must be unique.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Zone
        * *Description:* Name of a zone.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Must be part of the zones defined in the :ref:`Zones<target_zones>` sheet.

    ⚙️ Periode1, Periode2, ...
        * *Description:* Demand value for each period. Warning, this demand is in MWh/day and will be multiplied by the number of days in the period.
        * *Default value:* 0
        * *Default unit:* MWh/day
        * *Validity:* Float. The periods must be defined in the :ref:`Horizon<target_periods>` sheet.

.. _target_demand_transit:
.. admonition:: DemandeTransit - DEPRECIATED
    :class: error

    *Sheet description*: This sheet controls the global **daily** demand that can be offset from one PIR to another by period. This sheet is dynamic in a sense that you must add the periods define in your use case as columns. Please note that this module is depreciated and has not been used for a long time.

    .. list-table::
        :widths: 25 25 25 25 25 25
        :header-rows: 1

        * - Nom
          - PIR Amont
          - PIR Aval
          - Periode1
          - Periode2
          - ...
        * - Name1
          - UpstreamPIR1
          - DownstreamPIR1
          - Value11
          - Value21
          - ...
        * - Name2 
          - UpstreamPIR2
          - DownstreamPIR2
          - Value12
          - Value22
          - ...

    *Mandatory sheet*: ❌

.. _demand_transit:

    ⚙️ Nom
        * *Description:* Unique name of the demand.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ PIR Amont
        * *Description:* Name of the upstream PIR.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. The PIR must be defined in the :ref:`PIR<target_pir>` sheet.

    ⚙️ PIR Aval
        * *Description:* Name of the downstream PIR.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. The PIR must be defined in the :ref:`PIR<target_pir>` sheet.

    ⚙️ Periode1, Periode2, ...
        * *Description:* Demand value for each period. Warning, this demand is in MWh/day and will be multiplied by the number of days in the period.
        * *Default value:* 0
        * *Default unit:* MWh/day
        * *Validity:* Float. The periods must be defined in the :ref:`Horizon<target_periods>` sheet.

