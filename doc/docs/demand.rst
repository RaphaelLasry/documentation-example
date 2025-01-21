:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Demand
======

.. contents::
    :depth: 2
    :local:

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
        * *Validity:* Must be part of the zones defined in the :ref:`Zones<target_zones>` sheet.

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
.. admonition:: DemandeTransit
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