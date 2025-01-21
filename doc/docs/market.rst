:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Markets
=======

.. contents::
    :depth: 2
    :local:

Excel input sheets
------------------

.. _target_marches:
.. admonition:: Marches
    :class: error

    *Sheet Description*: This sheet controls the markets where the gas can be purchased or sold. The markets are defined by their name, delivery zone, maximum daily purchase, maximum daily sale, price and if they are the spot or not. Such modelling in Cactus is kind of dual to the classical way of using this tool. Here the goal is not to meet a demand but to optimize the purchase and sale of gas on the markets.

    .. list-table::
        :widths: 25 25 25 25 25 25
        :header-rows: 1

        * - marche	
          - livraison
          - max achat journalier [MWh/j]
          - max vente journalier [MWh/j]
          - prix [€/MWh]
          - spot {0,1}
        * - Market (ex: Market_FR)
          - Delivery zone (ex: FR)
          - Max daily purchase [MWh/d] (ex: Max_Buy_FR)
          - Max daily sale [MWh/d] (ex: 500)
          - Price [€/MWh] (ex: Prix_Market_FR)
          - Spot {0,1} (ex: 1)
    
    *Mandatory sheet*: ❌

.. _markets:

    ⚙️ marche
        * *Description:* Unique name of the market.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ livraison
        * *Description:* Delivery zone.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String

    ⚙️ max achat journalier [MWh/j]
        * *Description:* Maximum daily purchase.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`MaxMarches<target_max_marches>` sheet.

    ⚙️ max vente journalier [MWh/j]
        * *Description:* Maximum daily sale.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`MaxMarches<target_max_marches>` sheet.

    ⚙️ prix [€/MWh] 
        * *Description:* Price for purchasing or selling gas.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If String, then it must refer to a value defined in the :ref:`PrixApproParPdt<target_prix_appro_par_pdt>` sheet.

    ⚙️ spot {0,1}    
        * *Description:* Bollean to flag if the market is the *spot* or not.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Boolean

.. _target_max_marches:
.. admonition:: MaxMarches
    :class: error

    *Sheet Description*: This sheet let the user refine the data passed in the :ref:`Marches<target_marches>` sheet. The user can here provide a time series for the maximum daily purchase and sale of gas on the markets.

    .. list-table::
        :widths: 25 25 25
        :header-rows: 1

        * - Periode
          - Value1
          - Value2 
        * - Period (ex: 2020)
          - Value1 (ex: 500)
          - Value2 (ex: 1000)
    
    *Mandatory sheet*: ❌

.. _max_marches:

    ⚙️ Periode
        * *Description:* Unique index for the period.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date. It must refer to a value defined in the :ref:`Horizon<target_periods>` sheet.