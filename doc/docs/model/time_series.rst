:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Time Series
===========

.. contents::
    :depth: 2
    :local:

General introduction
--------------------

The times series module allow the user to serialize the data for each timestamp. The idea is that instead of having only one value the user could want to make it evolve through time. To do so, we use a system of index/key. It means that in some sheets it is possible to define a string instead of a float. This string will be used as a key to retrieve the value of the time series defined in the sheets below. As an example in the sheet :ref:`PIR<target_pir>` one of the parameter required is the price for the capacity (in or out). Such price could evolve trough time by putting a reference to a time series in the sheet :ref:`TarifParDate<target_tarif_par_date>`. Be aware that this does not make the model more complex at all as it's treated in the pre-processing phase.

Excel input sheets
------------------

.. _target_tarif_tm_par_date:
.. admonition:: TarifTMParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the price of the TM for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - TM_ZONE_1 (eg: 0.1)
          - TM_ZONE_2 (eg: 0.2)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Tariff value for each timestamp.
        * *Unit:* €/MWh
        * *Validity:* Float.

.. _target_capa_tm_par_date:
.. admonition:: CapaTMParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the capacity of the TM for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - Regaz_Capa_Fos Tonkin (eg: 35,000,000)
          - Regaz_Capa_Swinoujscie (eg: 58,670,100)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Capacity value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_tarif_tl_par_date:
.. admonition:: TarifTLParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the price of the TL for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - TL_ZONE_1 (eg: 0.1)
          - TL_ZONE_2 (eg: 0.2)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Tariff value for each timestamp.
        * *Unit:* €/MWh
        * *Validity:* Float.

.. _target_capa_lique_par_date:
.. admonition:: CapaLiqueParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the capacity of the Liquefaction Terminal for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - Lique_CA-West | Lique_LNG Canada (eg: 0)
          - Lique_ID-KP | Lique_Sengkang LNG (eg: 19,675)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Capacity value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_tarif_par_date:
.. admonition:: TarifParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the price of the PIR, PTM, Liaison and Transhipment for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - OGE PIR (eg: 0.47)
          - SortieVar_DE_PIR (eg: 0.04)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Tariff value for each timestamp.
        * *Unit:* €/MWh
        * *Validity:* Float.

.. _target_capa_par_pdt:
.. admonition:: CapaParPdt
    :class: error

    *Sheet Description*: This sheet is used to serialize the capacity of the interconnection point for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - Liaison_Canadian Mainline (eg: 1,050,019)
          - AddEntree_Amber Grid | LT | Kiemenai (eg: 65,100)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Capacity value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_volume_utile_par_date:
.. admonition:: VolumeUtileParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the useful volume for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - Volume_Fluxys - Loenhout (eg: 4,676,013)
          - AddVolume_Fluxys - Loenhout (eg: 3,163,987)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Volume value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_acq_par_date:
.. admonition:: AcqParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the annual quantity contract for each date.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - ACQ_LNG_QA>JP (eg: 127,200,000)
          - ACQ_LNG_QA>KW (eg: 37,100,000)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Annual quantity contract value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.
  
.. _target_dcq_par_pdt:
.. admonition:: DCQParPdt
    :class: error

    *Sheet Description*: This sheet is used to serialize the daily contract quantity for each product.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - DCQmin_LNG_DZ>FR (eg: 90)
          - DCQmax_LNG_DZ>FR (eg: 110)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Daily contract quantity value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_prix_appro_par_pdt:
.. admonition:: PrixApproParPdt
    :class: error

    *Sheet Description*: This sheet is used to serialize the purchase price for each appro contract.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ... 
        * - Date1 (eg: 01/01/2020)
          - PRIX_ZONE_1 (eg: 0.1)
          - PRIX_ZONE_2 (eg: 0.2)
          - ...

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Purchase price value for each timestamp.
        * *Unit:* €/MWh
        * *Validity:* Float.

.. _target_prod_max_par_date:
.. admonition:: ProdMaxParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the annual maximal production for each production plant.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Champ
          - Date
          - ProdAnnuelleMax
        * - Champ1 (eg: Alif Gas)
          - Date1 (eg: 01/01/2020)
          - Annual Maximal Production (eg: 1,000,000)

    ⚙️ Champ
        * *Description:* Name of the production plant.
        * *Unit:* *None*
        * *Validity:* String. Must be part of the productions defined in the :ref:`Champs<target_champs>` sheet.

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ ProdAnnuelleMax
        * *Description:* Annual maximal production value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_res_dev_max_par_date:
.. admonition:: ResDevMaxParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the maximum reserve deviation for each timestamp.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ...
        * - Date1 (eg: 01/01/2020)
          - RDM_002/05-03 (Tor Southeast) - Southeast Tor (eg: 0)
          - RDM_009/18A-40 (Garten) (eg: 3859857.871)
          - ... 
    
    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Maximum reserve deviation value for each timestamp. 
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_cout_prod_par_date:
.. admonition:: CoutProdParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the production cost for each timestamp.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ...
        * - Date1 (eg: 01/01/2020)
          - CoutProd1 (eg: 0)
          - CoutProd2 (eg: 10)
          - ... 

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Production cost value for each timestamp. 
        * *Unit:* €/MWh
        * *Validity:* Float.

.. _target_top_par_date:
.. admonition:: ToPParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the take or pay price for each timestamp.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Date
          - TimeSeries1
          - TimeSeries2
          - ...
        * - Date1 (eg: 01/01/2020)
          - TOP_United States (eg: 8,850,000,000)
          - TOP_Russia (eg: 7,200,000,000)
          - ... 

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ TimeSeries1, TimeSeries2, ...
        * *Description:* Take or Pay value for each timestamp. 
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_remplissage_pays_par_date:
.. admonition:: RemplissagePaysParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the aggregated level of stock (tunnel) for each country.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Pays
          - Date
          - NiveauxStockMin
          - NiveauxStockMax
        * - Pays1 (eg: France)
          - Date1 (eg: 01/01/2021)
          - Min level of stock (eg: 0)
          - Max level of stock (eg: 100)

    ⚙️ Pays
        * *Description:* Name of the country.
        * *Unit:* *None*
        * *Validity:* String. Must be part of the countries defined in the :ref:`ATS<target_ats>` sheet. If left blank, the country defined above will be used.

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ NiveauxStockMin
        * *Description:* Minimum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

    ⚙️ NiveauxStockMax
        * *Description:* Maximum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_remplissage_stockage_par_date:
.. admonition:: RemplissageStockageParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the level of stock (tunnel) for each storage.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Stockage
          - Date
          - NiveauxStockMin
          - NiveauxStockMax
        * - Stockage1 (eg: AM UGS)
          - Date1 (eg: 01/01/2021)
          - Min level of stock (eg: 47)
          - Max level of stock (eg: 93)

    ⚙️ Stockage
        * *Description:* Name of the storage.
        * *Unit:* *None*
        * *Validity:* String. Must be part of the storages defined in the :ref:`ATS<target_ats>` sheet. If left blank, the storage defined above will be used.

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ NiveauxStockMin
        * *Description:* Minimum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

    ⚙️ NiveauxStockMax
        * *Description:* Maximum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_remplissage_tm_par_date:
.. admonition:: RemplissageTMParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the level of stock (tunnel) for each TM.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - NomTM
          - Date
          - NiveauStockMin
          - NiveauStockMax
        * - NomTM1 (eg: Mejillones)
          - Date1 (eg: 01/01/2021)
          - Min level of stock (eg: 51)
          - Max level of stock (eg: 51)

    ⚙️ NomTM
        * *Description:* Name of the TM.
        * *Unit:* *None*
        * *Validity:* String. Must be part of the TMs defined in the :ref:`ATTM<target_attm>` sheet. If left blank, the TM defined above will be used.

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ NiveauStockMin
        * *Description:* Minimum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

    ⚙️ NiveauStockMax
        * *Description:* Maximum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

.. _target_remplissage_lique_par_date:
.. admonition:: RemplissageLiqueParDate
    :class: error

    *Sheet Description*: This sheet is used to serialize the level of stock (tunnel) for each liquefaction.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - NomLique
          - Date
          - NiveauStockMin
          - NiveauStockMax
        * - NomLique1 (eg: US-SC | Lique_Sabine Pass LNG)
          - Date1 (eg: 01/01/2021)
          - Min level of stock (eg: 80)
          - Max level of stock (eg: 81)

    ⚙️ NomLique
        * *Description:* Name of the liquefaction.
        * *Unit:* *None*
        * *Validity:* String. Must be part of the liquefactions defined in the :ref:`Lique<target_Lique>` sheet. If left blank, the liquefaction defined above will be used.

    ⚙️ Date
        * *Description:* Date of the times series.
        * *Unit:* *None*
        * *Validity:* Date

    ⚙️ NiveauStockMin
        * *Description:* Minimum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.

    ⚙️ NiveauStockMax
        * *Description:* Maximum level of stock value for each timestamp.
        * *Unit:* MWh
        * *Validity:* Float.