:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Global Parameters
=================

.. contents::
    :depth: 2
    :local:

Excel input sheets
------------------

.. _target_periods:

.. admonition:: Horizon
    :class: error

    *Sheet description*: Definition of the periods of the optimization horizon.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Periode
          - Date debut
          - Pointe (1)
        * - Index1 (ex: 1)
          - Date1 (ex: 01/01/2020)
          - BooleanPeak1 (ex: 0)
        * - Index2 (ex: 2)
          - Date2 (ex: 01/02/2020)
          - BooleanPeak2 (ex: 1)

    *Mandatory sheet*: ✅

.. _horizon:

    ⚙️ Periode
        * *Description:* Unique index for the period.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Integer

    ⚙️ Date debut
        * *Description:* Date of the beginning of the period.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* At least two periods must be defined. The granularity can be set up by the user (daily, weekly, monthly, yearly etc.).

    ⚙️ Pointe (1)
        * *Description:* Boolean that state whether the period is a peak period or not.
        * *Default value:* 0
        * *Default unit:* *None*
        * *Validity:* Boolean

.. _target_zones:

.. admonition:: Zones
    :class: error

    *Sheet description*: Topology of the simulation. The user can define all the zones (country, region or even virtual location) that will be used in the simulation. It is also here that the user defines the slack variables for the deficit and excess production of gas in the given zone.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Zones
          - Cout Deficit [€/MWh]
          - Cout Excedent [€/MWh]
        * - ZoneName1 (ex: FR)
          - DeficitCost1 (ex: 400)
          - ExcessCout1 (ex: 10)
        * - ZoneName2 (ex: FR-B)
          - DeficitCost2 (ex: 400)
          - ExcessCost2 (ex: 10)

    *Mandatory sheet*: ✅

.. _zones:

    ⚙️ Zones
        * *Description:* Name of the zone.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Cout Deficit [€/MWh]
        * *Description:* Value of the slack variable for the deficit (lost load).
        * *Default value:* *None* - Good practice is to set it up at 400 €/MWh.
        * *Default unit:* €/MWh
        * *Validity:* Float

    ⚙️ Cout Excedent [€/MWh]
        * *Description:* Value of the slack variable for the excess (curtailment).
        * *Default value:* *None* - Good practice is to set it up at 10 €/MWh.
        * *Default unit:* €/MWh
        * *Validity:* Float

.. _target_options:

.. admonition:: Options
    :class: error

    *Sheet description*: This sheet contains all the options that the user can set up for the simulation.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Option
          - Parameter
          - Value
        * - Option1 (ex: Ecart)
          - Parameter (ex: Activated)
          - Value (ex: 1)
        * - Option2 (ex: LNG)
          - Parameter (ex: Value)
          - Value (ex: 0)

    *Mandatory sheet*: ✅

.. _options:

    ⚙️ Option
        * *Description:* Name of the options. Note that such options can be skipped if not useful. The list of the options available is the following:
            
            - Ecart (Boolean): Use this option to activate the slack variables for the deficit and excess production of gas in the given zone. Note that if you don't use it the computational time might increase a lot as the problem becomes more tight.
            - LNG (Boolean): Use this option to activate the :doc:`LNG Shipping<shipping>` module. Basically it allows to consider duration of LNG trips between LNG Nodes instead of instantaneous transfer between any LNG nodes.
            - Monte-Carlo (Integer): Monte-Carlo simulation for the uncertainty of the demand. The number of simulations is controlled by the parameter in the code called `nb_iter`.
            - SDDP (String): Use this option to activate the Stochastic Dual Dynamic Programming (:doc:`SDDP<sddp>`) algorithm. This option is incompatible with the Monte-Carlo and the LNG one.
        
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Parameter
        * *Description:* Whether the option is *Activated* or *SDDP* specific ones. If the name of the option is *SDDP*, the user can specify different options in this field. When using SDDP algorithm, the user can select amongst those options:
  
            - Simulation (Boolean): Use this option to leverage on cuts that have already been built in a previous run.
            - Load Previous Cuts (Boolean): Load the cuts from a previous run (warm start). The algorithm will start from those cuts and build new ones on top.
            - Cuts Number (Integer): Number of cuts to build (mandatory option when using SDDP).
            - Max Rolling Cut Nb (Integer > 0): Cap the number of cuts to keep in memory for building the additionnal ones.
            - Workers Number (Integer, >= 2): Number of workers to use for the parallelization of the cuts.
  
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Value
        * *Description:* Boolean for activation of not of the option.
        * *Default value:* 0
        * *Default unit:* *None*
        * *Validity:* Boolean

.. _target_scalaire:

.. admonition:: Scalaire
    :class: error

    *Sheet description*: Scalar parameters usd in the simulation.

    .. list-table::
        :widths: 25 25 25 25 25 25 25
        :header-rows: 1

        * - Discount rate [% pa]
          - Cout Ecart [€/MWh]
          - Vessel Heel
          - BOR Standby Laden Ship [multiplier %]
          - Travel Max BOR [days]
          - Standby Max BOR [days]
          - Fixed Load Unload Time [days]
        * - Discount rate (ex: 0.05)
          - Slack Cost (ex: 10 000)
          - Vessel Heel (ex: 0.02)
          - BOR Stand by Laden Ship (ex: 0.75)
          - Travel Max BOR (ex: 40)
          - Standby Max BOR (ex: 90)
          - Fixed Load Unload Time (ex: 1)

    *Mandatory sheet*: ✅

.. _scalaire:

    ⚙️ Discount rate [% pa]
        * *Description:* Discount rate for the NPV calculation. Financial term that represent the depreciation of money `Discounting - Wikipedia <https://en.wikipedia.org/wiki/Discounting>`_. It means that 1€ in year +1 will be equivalent to 1€/r today.
        * *Default value:* *None*
        * *Default unit:* % pa
        * *Validity:* Float

    ⚙️ Cout Ecart [€/MWh]
        * *Description:* Value of the slack variable for the modelling variables (does not have any business meaning).
        * *Default value:* *None* - Good practice is to set it up at 10 000 €/MWh.
        * *Default unit:* €/MWh
        * *Validity:* Float

    ⚙️ Vessel Heel 
        * *Description:* Heel LNG is the quantity of LNG retained in the cargo to maintain their cryogenic temperatures. This parameter is used in the :doc:`LNG Shipping<shipping>` module and can be left empty if not used.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float

    ⚙️ BOR Standby Laden Ship [multiplier %]
        * *Description:* Boil-off rate (not due travel fueling), the amount of liquid that is evaporating from a cargo due to heat leakage and expressed in % of total liquid volume per unit time. This parameter is used in the :doc:`LNG Shipping<shipping>` module and can be left empty if not used.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float

    ⚙️ Travel Max BOR [days]
        * *Description:* Maximal number of days during which vessels can travel. This parameter is used in the :doc:`LNG Shipping<shipping>` module and can be left empty if not used.
        * *Default value:* *None*
        * *Default unit:* days
        * *Validity:* Integer

    ⚙️ Standby Max BOR [days]
        * *Description:* Maximal number of days during which vessels can be in standby. This parameter is used in the :doc:`LNG Shipping<shipping>` module and can be left empty if not used.
        * *Default value:* *None*
        * *Default unit:* days
        * *Validity:* Integer

    ⚙️ Fixed Load Unload Time [days]
        * *Description:* Fixed time for loading and unloading the LNG vessels. This parameter is used in the :doc:`LNG Shipping<shipping>` module and can be left empty if not used.
        * *Default value:* *None*
        * *Default unit:* days
        * *Validity:* Integer