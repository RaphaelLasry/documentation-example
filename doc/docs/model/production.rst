:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Production
==========

.. contents::
    :depth: 2
    :local:

Excel input sheets
------------------

Gas supply
^^^^^^^^^^

.. _target_appros:
.. admonition:: Appros
    :class: error

    *Sheet Description*: This sheet controls the gas contracts. Each contract is defined by its name, the minimum and maximum annual contracted volume, the gas price, the minimum and maximum daily contracted volume, the flexibility mode and the yearly volume contracted. With such object the user can define gas supply in the model.

    .. list-table::
        :widths: 25 25 25 25 25 25 25 25
        :header-rows: 1

        * - contrat
          - ACQ Min [%]
          - ACQ Max [%]
          - prix volume [€/MWh]
          - DCQ Min [%]
          - DCQ Max [%]
          - Mode de calcul de la flexibilite
          - Volume annuel [MWh]
        * - Contract (ex: Prod NO)
          - ACQ Min (ex: 0)
          - ACQ Max (ex: 100)
          - Gas price (ex: 50)
          - DCQ Min (ex: DCQmin_Prod NO)
          - DCQ Max (ex: 100)
          - Flexibility mode (ex: 1)
          - Yearly volume (ex: ACQ_Prod NO)

    *Mandatory sheet*: ❌

.. _appros:

    ⚙️ contrat
        * *Description:* Unique name of the contract.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ ACQ Min [%]
        * *Description:* Minimum *Annual Contract Quantity*. Minimum percentage of annual volume contracted that the system must consume.
        * *Default value:* 0
        * *Default unit:* %
        * *Validity:* Float

    ⚙️ ACQ Max [%]
        * *Description:* Maximum *Annual Contract Quantity*. Maximum percentage of annual volume contracted that the system must consume.
        * *Default value:* 100
        * *Default unit:* %
        * *Validity:* Float

    ⚙️ prix volume [€/MWh]
        * *Description:* Price of the gas volume.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`PrixApproParPdt<target_prix_appro_par_pdt>` sheet.

    ⚙️ DCQ Min [%]
        * *Description:* Minimum *Daily Contract Quantity*. Minimum percentage of daily volume contracted that the system must consume. Daily volume contracted corresponds to the ACQ / 365.
        * *Default value:* 0
        * *Default unit:* %
        * *Validity:* Float or Sting. If String, then it must refer to a value defined in the :ref:`DCQParPdt<target_dcq_par_pdt>` sheet.

    ⚙️ DCQ Max [%]
        * *Description:* Maximum *Daily Contract Quantity*. Maximum percentage of daily volume contracted that the system must consume. Daily volume contracted corresponds to the ACQ / 365.
        * *Default value:* 100
        * *Default unit:* %
        * *Validity:* Float or Sting. If String, then it must refer to a value defined in the :ref:`DCQParPdt<target_dcq_par_pdt>` sheet.

    ⚙️ Mode de calcul de la flexibilite
        * *Description:* Integer that map the flexibility calculus. It can be 0, 1 or 2.
            * 0: The contracted part should respect ACQ Min/Max constraints as well as DCQ Min/Max constraints. The model chooses both the annual and daily contracted volumes. The size of the strip around the daily volume is proportional to the latter.
            * 1: Differ from the previous option as the annual volume is now fixed (exogenous), and the model can choose the daily contracted volume but can't choose the size of the strip around this daily volume (which depends on the exogenous annual volume).
            * 2: This is the less flexible option for the model can't choose neither the daily volume nor the size of the strip around it.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Integer

    ⚙️ Volume annuel [MWh]
        * *Description:* Annual volume contracted.
        * *Default value:* *None*
        * *Default unit:* MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`ACQParDate<target_acq_par_date>` sheet.

.. _target_raccordements_appros:
.. admonition:: RaccordementsAppros
    :class: error

    *Sheet Description*: This sheet controls the connection points of the contracts. Each contract should be linked to a pipe, a liquefaction terminal or a regasification terminal.

    .. list-table::
        :widths: 25 25
        :header-rows: 1

        * - contrat	
          - livraison (PIR, PTM, TM)
        * - Contract (ex: Prod NO)
          - Connection point (ex: NO | Production)

    *Mandatory sheet*: ❌

.. _raccordements_appros:

    ⚙️ contrat
        * *Description:* Unique name of the contract.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the contracts defined in the :ref:`Appros<appros>` sheet.

    ⚙️ livraison (PIR, PTM, TM)
        * *Description:* Delivery point of the contract. Each appros should either be linked to a pipe, a liquefaction terminal or a regasification terminal.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the connection points defined in the :ref:`PIR<target_pir>`, :ref:`PTM<target_ptm>` or :ref:`TM<target_tm>` sheets.

Gas fields
^^^^^^^^^^

.. _target_perimetres_production:
.. admonition:: PerimetresProd
    :class: error

    *Sheet Description*: This sheet controls the production areas. Each production area is defined by its name and the annual Take-or-Pay quantity. Please note that the areas and the zones are two different un-related spatial dimensions in Cactus. They are linked by the objects PIR.

    .. list-table::
        :widths: 25 25
        :header-rows: 1

        * - Périmètre de production
          - Quantité annuelle Take-or-Pay
        * - Production area (ex: Libya)
          - Take-or-Pay annual quantity (ex: TOP_Libya)

    *Mandatory sheet*: ❌

.. _perimetres_production:

    ⚙️ Périmètre de production
        * *Description:* Name of the production area.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Quantité annuelle Take-or-Pay
        * *Description:* Annual Take-or-Pay quantity.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`ToPParDate<target_top_par_date>` sheet.

.. _target_champs:

.. admonition:: Champs
    :class: error

    *Sheet Description*: This sheet controls the fields. Each field is defined by its name, the production area, the connection point, the minimum and maximum daily contract quantity, the initial and maximum developed reserves, the development and dismantling CAPEX, the variable and fixed OPEX, the discounted cost of residual developed capacity and the residual gas NPV. It's another way of modelling gas supply. Here the goal is to represent the physical gas plant as well as the quantity available in such a plant.

    .. list-table::
        :widths: 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 
        :header-rows: 1

        * - Champ
          - Périmètre de production
          - PIR de raccordement
          - DCQ Min [%]
          - DCQ Max [%]
          - DCQ Min à la pointe [%]
          - DCQ Max à la pointe [%]
          - Réserves développées initiales [MWh]
          - Réserves développées max [MWh]
          - CAPEX développement [€/MWh]
          - CAPEX démantèlement [€/MWh]
          - OPEX Variable [€/MWh]
          - OPEX Fixe [€/MWh]
          - Coût actualisé capa développée résiduelle [€/MWh]
          - VAN du gaz résiduel [€/MWh]
        * - Field (ex: 097-TAMAR)
          - Production area (ex: Libya)
          - Connection point (ex: LY | Production)
          - DCQ Min (ex: 65)
          - DCQ Max (ex: 106)
          - DCQ Min at peak (ex: 65)
          - DCQ Max at peak (ex: 106)
          - Initial developed reserves (ex: 4 500 000)
          - Maximum developed reserves (ex: RDM_097-T)
          - CAPEX development (ex: 0)
          - CAPEX dismantling (ex:0.01)
          - OPEX Variable (ex: 0.18)
          - OPEX Fixed (ex: 0.01)
          - Discounted cost of residual developed capacity (ex: 0)
          - Residual gas NPV (ex: 0.68)

    *Mandatory sheet*: ❌

.. _champs:

    ⚙️ Champ
        * *Description:* Unique name of the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ Périmètre de production
        * *Description:* Production area of the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Should be part of the production areas defined in the :ref:`PerimetresProd<target_perimetres_production>` sheet.

    ⚙️ PIR de raccordement
        * *Description:* Connection point of the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the connection points defined in the :ref:`PIR<target_pir>` sheet.

    ⚙️ DCQ Min [%]
        * *Description:* Minimum *Daily Contract Quantity*. Minimum percentage of daily volume contracted that the system must consume. Daily volume contracted corresponds to the ACQ / 365.
        * *Default value:* 0
        * *Default unit:* %
        * *Validity:* Float

    ⚙️ DCQ Max [%]
        * *Description:* Maximum *Daily Contract Quantity*. Maximum percentage of daily volume contracted that the system must consume. Daily volume contracted corresponds to the ACQ / 365.
        * *Default value:* 100
        * *Default unit:* %
        * *Validity:* Float

    ⚙️ DCQ Min à la pointe [%]
        * *Description:* Minimum *Daily Contract Quantity* at peak. Minimum percentage of daily volume contracted that the system must consume at peak. Daily volume contracted corresponds to the ACQ / 365.
        * *Default value:* 0
        * *Default unit:* %
        * *Validity:* Float

    ⚙️ DCQ Max à la pointe [%]
        * *Description:* Maximum *Daily Contract Quantity* at peak. Maximum percentage of daily volume contracted that the system must consume at peak. Daily volume contracted corresponds to the ACQ / 365.
        * *Default value:* 100
        * *Default unit:* %
        * *Validity:* Float

    ⚙️ Réserves développées initiales [MWh]
        * *Description:* Initial developed reserves of the field.
        * *Default value:* *None*
        * *Default unit:* MWh
        * *Validity:* Float

    ⚙️ Réserves développées max [MWh]
        * *Description:* Maximum developed reserves of the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`ResDevMaxParDate<target_res_dev_max_par_date>` sheet.

    ⚙️ CAPEX développement [€/MWh]
        * *Description:* Development CAPEX of the field.
        * *Default value:* 0
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`CoutProdParDate<target_cout_prod_par_date>` sheet.

    ⚙️ CAPEX démantèlement [€/MWh]
        * *Description:* Dismantling CAPEX of the field.
        * *Default value:* 0
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`CoutProdParDate<target_cout_prod_par_date>` sheet.

    ⚙️ OPEX Variable [€/MWh]
        * *Description:* Variable OPEX of the field.
        * *Default value:* 0
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`CoutProdParDate<target_cout_prod_par_date>` sheet.

    ⚙️ OPEX Fixe [€/MWh]   
        * *Description:* Fixed OPEX of the field.
        * *Default value:* 0
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`CoutProdParDate<target_cout_prod_par_date>` sheet.

    ⚙️ Coût actualisé capa développée résiduelle [€/MWh]
        * *Description:* Discounted cost of residual developed capacity.
        * *Default value:* 0
        * *Default unit:* €/MWh
        * *Validity:* Float

    ⚙️ VAN du gaz résiduel [€/MWh]
        * *Description:* Residual gas NPV.
        * *Default value:* 0
        * *Default unit:* €/MWh
        * *Validity:* Float

.. _target_contraintes_prod:
.. admonition:: ContraintesProd
    :class: error

    *Sheet Description*: This sheet controls the production constraints. Each constraint is defined by its name, the origin level and the slope for the evolution of the gas in the field. It allows the user to define the evolution of the gas in the field.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Champ
          - Origine
          - Pente 
        * - Champ (ex: 097-T)
          - Origin (ex: 0.38)
          - Slope (ex: -0.13)

    *Mandatory sheet*: ❌

.. _contraintes_prod:

    ⚙️ Champ
        * *Description:* Unique name of the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the fields defined in the :ref:`Champs<champs>` sheet.

    ⚙️ Origine
        * *Description:* Origin level of the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float

    ⚙️ Pente
        * *Description:* Slope for the evolution of the gas in the field.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float