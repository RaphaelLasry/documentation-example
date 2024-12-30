:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Demand
======

.. contents::
    :depth: 2
    :local:

Excel input sheets
------------------



.. admonition:: DemandeNormale
    :class: note

    *Sheet description*: This sheet controls the global **daily** demand by zone on each time period. This sheet is dynamic in a sense that you must add the periods define in your use case as columns.

    .. list-table::
        :widths: 25 25 25 25 25
        :header-rows: 1

        * - Nom
          - Zone
          - Periode1
          - Periode2
          - ...
        * - NomDemande1
          - NomZone1
          - Value11
          - Value21
          - ...
        * - NomDemande2
          - NomZone2
          - Value12
          - Value22
          - ...

    *Mandatory sheet*: ❌

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