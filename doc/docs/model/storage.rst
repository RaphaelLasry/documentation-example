:orphan:  .. NOT DELETE: Avoid warning about document not being included in any toctree

Storage
=======

.. contents::
    :depth: 2
    :local:

Excel input sheets
------------------

Gas storage
^^^^^^^^^^^

.. _target_ats:
.. admonition:: ATS
    :class: error

    *Sheet Description*: The ATS sheet contains the parameters of the storage. It's the place where an object storage is defined with its characteristics (price and capacity mainly).

    .. list-table::
        :widths: 25 25 25 25 25 25 25 25 25 25 25 25 25
        :header-rows: 1

        * - Pays
          - NomStockage
          - prix d'injection [€/MWh]
          - prix de soutirage [€/MWh]
          - Prix du volume nominal [€/MWh]
          - % soutirage supplementaire à la pointe
          - Volume admissible [MWh]
          - Duree de soutirage [j]
          - Duree d'injection [j]
          - Mois démarrage année stockage
          - Volume admissible dispo [MWh]
          - Palier Injection (0,1)
          - Palier Soutirage (0,1)
        * - Country (eg: World)
          - Name of the storage (eg: Fluxys - Loenhout)
          - Injection price [€/MWh] (eg: 0.15)
          - Withdrawal price [€/MWh] (eg: 0.08)
          - Nominal volume price [€/MWh] (eg: 3.33)
          - Additional withdrawal percentage at peak (eg: 0)
          - Admissible volume [MWh] (eg: Volume_Fluxys - Loenhout)
          - Withdrawal duration [days] (eg: 52)
          - Injection duration [days] (eg: 100)
          - Storage start month (eg: 4)
          - Available admissible volume [MWh] (eg: AddVolume_Fluxys - Loenhout)
          - Injection level (0,1) (eg: 1)
          - Withdrawal level (0,1) (eg: 1)

.. _ats:

    ⚙️ Pays
        * *Description:* The country where the storage is located.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String.

    ⚙️ NomStockage
        * *Description:* The name of the storage.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String.

    ⚙️ prix d'injection [€/MWh]
        * *Description:* The price of injection.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float.

    ⚙️ prix de soutirage [€/MWh]
        * *Description:* The price of withdrawal.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float.

    ⚙️ Prix du volume nominal [€/MWh]
        * *Description:* The price of the nominal volume.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float.

    ⚙️ % soutirage supplementaire à la pointe
        * *Description:* The additional withdrawal percentage at peak.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Volume admissible [MWh]
        * *Description:* The admissible volume.
        * *Default value:* *None*
        * *Default unit:* MWh
        * *Validity:* Float or String. If string, it must be part of the :ref:`VolumeUtileParDate<target_volume_utile_par_date>` sheet.

    ⚙️ Duree de soutirage [j]
        * *Description:* The withdrawal duration.
        * *Default value:* *None*
        * *Default unit:* days
        * *Validity:* Integer.

    ⚙️ Duree d'injection [j]
        * *Description:* The injection duration.
        * *Default value:* *None*
        * *Default unit:* days
        * *Validity:* Integer.

    ⚙️ Mois démarrage année stockage
        * *Description:* The storage start month.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Integer.

    ⚙️ Volume admissible dispo [MWh]
        * *Description:* The available admissible volume.
        * *Default value:* *None*
        * *Default unit:* MWh
        * *Validity:* Float or String. If string, it must be part of the :ref:`VolumeUtileParDate<target_volume_utile_par_date>` sheet.

    ⚙️ Palier Injection (0,1)
        * *Description:* The injection level.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Boolean.

    ⚙️ Palier Soutirage (0,1)
        * *Description:* The withdrawal level.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Boolean.

.. _target_pits:

.. admonition:: PITS
    :class: error

    *Sheet Description*: The PITS (Point d'Interconnexion Transport Stockage) sheet contains the parameters for the link between the storage and the rest of the system. It's another place to control the quatity available in the storage (capacity of injection/withdrawal) as well as the price of it.

    .. list-table::
        :widths: 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25 25
        :header-rows: 1

        * - Nom
          - zone
          - Capacité souscrite en entrée [MWh/j]
          - Capacité dispo en entrée [MWh/j]
          - Capacité souscrite en sortie [MWh/j]
          - Capacité dispo en sortie [MWh/j]
          - Part de la capacité d'entrée à mettre de côté pour le court terme [%]
          - Part de la capacité de sortie à mettre de côté pour le court terme [%]
          - Mois démarrage capas annuelles
          - Début modélisation capas annuelles entrée
          - Début modélisation capas annuelles sortie
          - Début modélisation capas trimestrielles entrée
          - Début modélisation capas trimestrielles sortie
          - Début modélisation capas mensuelles entrée
          - Début modélisation capas mensuelles sortie
          - Début modélisation capas journalières entrée
          - Début modélisation capas journalières sortie
          - Fin modélisation capas annuelles entrée
          - Fin modélisation capas annuelles sortie
          - Fin modélisation capas trimestrielles entrée
          - Fin modélisation capas trimestrielles sortie
          - Fin modélisation capas mensuelles entrée
          - Fin modélisation capas mensuelles sortie
          - Fin modélisation capas journalières entrée
          - Fin modélisation capas journalières sortie
          - Tarif Capacite entree [€/MWh/j]
          - Tarif Capacite sortie [€/MWh/j]
          - Tarif Variable entree [€/MWh]
          - Tarif Variable sortie [€/MWh]
          - Gas-in-kind entrée [%]
          - Gas-in-kind sortie [%]
          - Multiplicateur trimestriel Tarif Capa d'entrée
          - Multiplicateur mensuel Tarif Capa d'entrée
          - Multiplicateur journalier Tarif Capa d'entrée
          - Multiplicateur trimestriel Tarif Capa de sortie
          - Multiplicateur mensuel Tarif Capa de sortie
          - Multiplicateur journalier Tarif Capa de sortie
          - Facteur saisonnier trimestriel entrée Q1
          - Facteur saisonnier trimestriel entrée Q2
          - Facteur saisonnier trimestriel entrée Q3
          - Facteur saisonnier trimestriel entrée Q4
          - Facteur saisonnier trimestriel sortie Q1
          - Facteur saisonnier trimestriel sortie Q2
          - Facteur saisonnier trimestriel sortie Q3
          - Facteur saisonnier trimestriel sortie Q4
          - Facteur saisonnier mensuel entrée Janvier
          - Facteur saisonnier mensuel entrée Février
          - Facteur saisonnier mensuel entrée Mars
          - Facteur saisonnier mensuel entrée Avril
          - Facteur saisonnier mensuel entrée Mai
          - Facteur saisonnier mensuel entrée Juin
          - Facteur saisonnier mensuel entrée Juillet
          - Facteur saisonnier mensuel entrée Août
          - Facteur saisonnier mensuel entrée Septembre
          - Facteur saisonnier mensuel entrée Octobre
          - Facteur saisonnier mensuel entrée Novembre
          - Facteur saisonnier mensuel entrée Décembre
          - Facteur saisonnier mensuel sortie Janvier
          - Facteur saisonnier mensuel sortie Février
          - Facteur saisonnier mensuel sortie Mars
          - Facteur saisonnier mensuel sortie Avril
          - Facteur saisonnier mensuel sortie Mai
          - Facteur saisonnier mensuel sortie Juin
          - Facteur saisonnier mensuel sortie Juillet
          - Facteur saisonnier mensuel sortie Août
          - Facteur saisonnier mensuel sortie Septembre
          - Facteur saisonnier mensuel sortie Octobre
          - Facteur saisonnier mensuel sortie Novembre
          - Facteur saisonnier mensuel sortie Décembre
          - Facteur saisonnier journalier entrée Janvier
          - Facteur saisonnier journalier entrée Février
          - Facteur saisonnier journalier entrée Mars
          - Facteur saisonnier journalier entrée Avril
          - Facteur saisonnier journalier entrée Mai
          - Facteur saisonnier journalier entrée Juin
          - Facteur saisonnier journalier entrée Juillet
          - Facteur saisonnier journalier entrée Août
          - Facteur saisonnier journalier entrée Septembre
          - Facteur saisonnier journalier entrée Octobre
          - Facteur saisonnier journalier entrée Novembre
          - Facteur saisonnier journalier entrée Décembre
          - Facteur saisonnier journalier sortie Janvier
          - Facteur saisonnier journalier sortie Février
          - Facteur saisonnier journalier sortie Mars
          - Facteur saisonnier journalier sortie Avril
          - Facteur saisonnier journalier sortie Mai
          - Facteur saisonnier journalier sortie Juin
          - Facteur saisonnier journalier sortie Juillet
          - Facteur saisonnier journalier sortie Août
          - Facteur saisonnier journalier sortie Septembre
          - Facteur saisonnier journalier sortie Octobre
          - Facteur saisonnier journalier sortie Novembre
          - Facteur saisonnier journalier sortie Décembre
        * - Name (eg: bayernets | DE-NCG | Haidach)
          - zone (eg: DE-H)
          - Subscribed entry capacity [MWh/d] (eg: Entree_bayernets | DE-NCG | Haidach)
          - Available entry capacity [MWh/d] (eg: AddEntree_bayernets | DE-NCG | Haidach)
          - Subscribed exit capacity [MWh/d] (eg: Sortie_bayernets | DE-NCG | Haidach)
          - Available exit capacity [MWh/d] (eg: AddSortie_bayernets | DE-NCG | Haidach)
          - Percentage of entry capacity set aside for short term [%] (eg: 0%)
          - Percentage of exit capacity set aside for short term [%] (eg: 0%)
          - Annual capacity start month (eg: 10)
          - Annual capacity modeling start date (eg: 1/1/2020)
          - Annual capacity modeling end date (eg: 1/1/2100)
          - Quarterly capacity modeling start date (eg: 1/1/2020)
          - Quarterly capacity modeling end date (eg: 1/1/2100)
          - Monthly capacity modeling start date (eg: 1/1/2020)
          - Monthly capacity modeling end date (eg: 1/1/2100)
          - Daily capacity modeling start date (eg: 1/1/2020)
          - Daily capacity modeling end date (eg: 1/1/2100)
          - Entry capacity tariff [€/MWh/d] (eg: 0.115519135)
          - Exit capacity tariff [€/MWh/d] (eg: 0.095880855)
          - Variable entry tariff [€/MWh] (eg: 0)
          - Variable exit tariff [€/MWh] (eg: 0)
          - Gas-in-kind entry [%] (eg: 0%)
          - Gas-in-kind exit [%] (eg: 0%)
          - Quarterly entry capacity tariff multiplier (eg: 1.1)
          - Monthly entry capacity tariff multiplier (eg: 1.25)
          - Daily entry capacity tariff multiplier (eg: 1.4)
          - Quarterly exit capacity tariff multiplier (eg: 1.1)
          - Monthly exit capacity tariff multiplier (eg: 1.25)
          - Daily exit capacity tariff multiplier (eg: 1.4)
          - Quarterly seasonal factor entry Q1 (eg: 1)
          - Quarterly seasonal factor entry Q2 (eg: 1)
          - Quarterly seasonal factor entry Q3 (eg: 1)
          - Quarterly seasonal factor entry Q4 (eg: 1)
          - Quarterly seasonal factor exit Q1 (eg: 1)
          - Quarterly seasonal factor exit Q2 (eg: 1)
          - Quarterly seasonal factor exit Q3 (eg: 1)
          - Quarterly seasonal factor exit Q4 (eg: 1)
          - Monthly seasonal factor entry January (eg: 1)
          - Monthly seasonal factor entry February (eg: 1)
          - Monthly seasonal factor entry March (eg: 1)
          - Monthly seasonal factor entry April (eg: 1)
          - Monthly seasonal factor entry May (eg: 1)
          - Monthly seasonal factor entry June (eg: 1)
          - Monthly seasonal factor entry July (eg: 1)
          - Monthly seasonal factor entry August (eg: 1)
          - Monthly seasonal factor entry September (eg: 1)
          - Monthly seasonal factor entry October (eg: 1)
          - Monthly seasonal factor entry November (eg: 1)
          - Monthly seasonal factor entry December (eg: 1)
          - Monthly seasonal factor exit January (eg: 1)
          - Monthly seasonal factor exit February (eg: 1)
          - Monthly seasonal factor exit March (eg: 1)
          - Monthly seasonal factor exit April (eg: 1)
          - Monthly seasonal factor exit May (eg: 1)
          - Monthly seasonal factor exit June (eg: 1)
          - Monthly seasonal factor exit July (eg: 1)
          - Monthly seasonal factor exit August (eg: 1)
          - Monthly seasonal factor exit September (eg: 1)
          - Monthly seasonal factor exit October (eg: 1)
          - Monthly seasonal factor exit November (eg: 1)
          - Monthly seasonal factor exit December (eg: 1)
          - Daily seasonal factor entry January (eg: 1)
          - Daily seasonal factor entry February (eg: 1)
          - Daily seasonal factor entry March (eg: 1)
          - Daily seasonal factor entry April (eg: 1)
          - Daily seasonal factor entry May (eg: 1)
          - Daily seasonal factor entry June (eg: 1)
          - Daily seasonal factor entry July (eg: 1)
          - Daily seasonal factor entry August (eg: 1)
          - Daily seasonal factor entry September (eg: 1)
          - Daily seasonal factor entry October (eg: 1)
          - Daily seasonal factor entry November (eg: 1)
          - Daily seasonal factor entry December (eg: 1)
          - Daily seasonal factor exit January (eg: 1)
          - Daily seasonal factor exit February (eg: 1)
          - Daily seasonal factor exit March (eg: 1)
          - Daily seasonal factor exit April (eg: 1)
          - Daily seasonal factor exit May (eg: 1)
          - Daily seasonal factor exit June (eg: 1)
          - Daily seasonal factor exit July (eg: 1)
          - Daily seasonal factor exit August (eg: 1)
          - Daily seasonal factor exit September (eg: 1)
          - Daily seasonal factor exit October (eg: 1)
          - Daily seasonal factor exit November (eg: 1)
          - Daily seasonal factor exit December (eg: 1)

.. _pits:

    ⚙️ Nom
        * *Description:* The name of the storage.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String.

    ⚙️ zone
        * *Description:* The zone where the storage is located.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`Zone<target_zone>` sheet.

    ⚙️ Capacité souscrite en entrée [MWh/j]
        * *Description:* The subscribed entry capacity.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float or String. If string, it must be part of the :ref:`CapaParPdt<target_capa_par_pdt>` sheet.

    ⚙️ Capacité dispo en entrée [MWh/j]
        * *Description:* The available entry capacity.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float or String. If string, it must be part of the :ref:`CapaParPdt<target_capa_par_pdt>` sheet.

    ⚙️ Capacité souscrite en sortie [MWh/j]
        * *Description:* The subscribed exit capacity.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float or String. If string, it must be part of the :ref:`CapaParPdt<target_capa_par_pdt>` sheet.

    ⚙️ Capacité dispo en sortie [MWh/j]
        * *Description:* The available exit capacity.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float or String. If string, it must be part of the :ref:`CapaParPdt<target_capa_par_pdt>` sheet.

    ⚙️ Part de la capacité d'entrée à mettre de côté pour le court terme [%]
        * *Description:* The percentage of entry capacity set aside for short term.
        * *Default value:* *None*
        * *Default unit:* %
        * *Validity:* Float.

    ⚙️ Part de la capacité de sortie à mettre de côté pour le court terme [%]
        * *Description:* The percentage of exit capacity set aside for short term.
        * *Default value:* *None*
        * *Default unit:* %
        * *Validity:* Float.

    ⚙️ Mois démarrage capas annuelles
        * *Description:* The annual capacity start month.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Integer.

    ⚙️ Début modélisation capas annuelles entrée
        * *Description:* The annual capacity modeling start date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas annuelles sortie
        * *Description:* The annual capacity modeling start date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas trimestrielles entrée
        * *Description:* The quarterly capacity modeling start date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas trimestrielles sortie
        * *Description:* The quarterly capacity modeling start date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas mensuelles entrée
        * *Description:* The monthly capacity modeling start date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas mensuelles sortie
        * *Description:* The monthly capacity modeling start date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas journalières entrée
        * *Description:* The daily capacity modeling start date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Début modélisation capas journalières sortie
        * *Description:* The daily capacity modeling start date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas annuelles entrée
        * *Description:* The annual capacity modeling end date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas annuelles sortie
        * *Description:* The annual capacity modeling end date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas trimestrielles entrée
        * *Description:* The quarterly capacity modeling end date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas trimestrielles sortie
        * *Description:* The quarterly capacity modeling end date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas mensuelles entrée
        * *Description:* The monthly capacity modeling end date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas mensuelles sortie
        * *Description:* The monthly capacity modeling end date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas journalières entrée
        * *Description:* The daily capacity modeling end date for entry.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin modélisation capas journalières sortie
        * *Description:* The daily capacity modeling end date for exit.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Tarif Capacite entree [€/MWh/j]
        * *Description:* The entry capacity tariff.
        * *Default value:* *None*
        * *Default unit:* €/MWh/d
        * *Validity:* Float or String. If string, it must be part of the :ref:`TarifParDate<target_tarif_par_date>` sheet.

    ⚙️ Tarif Capacite sortie [€/MWh/j]
        * *Description:* The exit capacity tariff.
        * *Default value:* *None*
        * *Default unit:* €/MWh/d
        * *Validity:* Float or String. If string, it must be part of the :ref:`TarifParDate<target_tarif_par_date>` sheet.

    ⚙️ Tarif Variable entree [€/MWh]
        * *Description:* The variable entry tariff.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If string, it must be part of the :ref:`TarifParDate<target_tarif_par_date>` sheet.

    ⚙️ Tarif Variable sortie [€/MWh]
        * *Description:* The variable exit tariff.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If string, it must be part of the :ref:`TarifParDate<target_tarif_par_date>` sheet.

    ⚙️ Gas-in-kind entrée [%]
        * *Description:* The gas-in-kind entry percentage.
        * *Default value:* *None*
        * *Default unit:* %
        * *Validity:* Float.

    ⚙️ Gas-in-kind sortie [%]
        * *Description:* The gas-in-kind exit percentage.
        * *Default value:* *None*
        * *Default unit:* %
        * *Validity:* Float.

    ⚙️ Multiplicateur trimestriel Tarif Capa d'entrée
        * *Description:* The quarterly entry capacity tariff multiplier.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Multiplicateur mensuel Tarif Capa d'entrée
        * *Description:* The monthly entry capacity tariff multiplier.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Multiplicateur journalier Tarif Capa d'entrée
        * *Description:* The daily entry capacity tariff multiplier.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Multiplicateur trimestriel Tarif Capa de sortie
        * *Description:* The quarterly exit capacity tariff multiplier.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Multiplicateur mensuel Tarif Capa de sortie
        * *Description:* The monthly exit capacity tariff multiplier.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Multiplicateur journalier Tarif Capa de sortie
        * *Description:* The daily exit capacity tariff multiplier.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel entrée Q1
        * *Description:* The quarterly seasonal factor for entry in Q1.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel entrée Q2
        * *Description:* The quarterly seasonal factor for entry in Q2.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel entrée Q3
        * *Description:* The quarterly seasonal factor for entry in Q3.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel entrée Q4
        * *Description:* The quarterly seasonal factor for entry in Q4.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel sortie Q1
        * *Description:* The quarterly seasonal factor for exit in Q1.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel sortie Q2
        * *Description:* The quarterly seasonal factor for exit in Q2.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel sortie Q3
        * *Description:* The quarterly seasonal factor for exit in Q3.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier trimestriel sortie Q4
        * *Description:* The quarterly seasonal factor for exit in Q4.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Janvier
        * *Description:* The monthly seasonal factor for entry in January.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Février
        * *Description:* The monthly seasonal factor for entry in February.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Mars
        * *Description:* The monthly seasonal factor for entry in March.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Avril
        * *Description:* The monthly seasonal factor for entry in April.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Mai
        * *Description:* The monthly seasonal factor for entry in May.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Juin
        * *Description:* The monthly seasonal factor for entry in June.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Juillet
        * *Description:* The monthly seasonal factor for entry in July.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Août
        * *Description:* The monthly seasonal factor for entry in August.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Septembre
        * *Description:* The monthly seasonal factor for entry in September.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Octobre
        * *Description:* The monthly seasonal factor for entry in October.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Novembre
        * *Description:* The monthly seasonal factor for entry in November.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel entrée Décembre
        * *Description:* The monthly seasonal factor for entry in December.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Janvier
        * *Description:* The monthly seasonal factor for exit in January.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Février
        * *Description:* The monthly seasonal factor for exit in February.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Mars
        * *Description:* The monthly seasonal factor for exit in March.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Avril
        * *Description:* The monthly seasonal factor for exit in April.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Mai
        * *Description:* The monthly seasonal factor for exit in May.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Juin
        * *Description:* The monthly seasonal factor for exit in June.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Juillet
        * *Description:* The monthly seasonal factor for exit in July.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Août
        * *Description:* The monthly seasonal factor for exit in August.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Septembre
        * *Description:* The monthly seasonal factor for exit in September.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Octobre
        * *Description:* The monthly seasonal factor for exit in October.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Novembre
        * *Description:* The monthly seasonal factor for exit in November.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier mensuel sortie Décembre
        * *Description:* The monthly seasonal factor for exit in December.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Janvier
        * *Description:* The daily seasonal factor for entry in January.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Février
        * *Description:* The daily seasonal factor for entry in February.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Mars
        * *Description:* The daily seasonal factor for entry in March.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Avril
        * *Description:* The daily seasonal factor for entry in April.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Mai
        * *Description:* The daily seasonal factor for entry in May.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Juin
        * *Description:* The daily seasonal factor for entry in June.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Juillet
        * *Description:* The daily seasonal factor for entry in July.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Août
        * *Description:* The daily seasonal factor for entry in August.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Septembre
        * *Description:* The daily seasonal factor for entry in September.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Octobre
        * *Description:* The daily seasonal factor for entry in October.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Novembre
        * *Description:* The daily seasonal factor for entry in November.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier entrée Décembre
        * *Description:* The daily seasonal factor for entry in December.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Janvier
        * *Description:* The daily seasonal factor for exit in January.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Février
        * *Description:* The daily seasonal factor for exit in February.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Mars
        * *Description:* The daily seasonal factor for exit in March.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Avril
        * *Description:* The daily seasonal factor for exit in April.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Mai
        * *Description:* The daily seasonal factor for exit in May.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Juin
        * *Description:* The daily seasonal factor for exit in June.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Juillet
        * *Description:* The daily seasonal factor for exit in July.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Août
        * *Description:* The daily seasonal factor for exit in August.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Septembre
        * *Description:* The daily seasonal factor for exit in September.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Octobre
        * *Description:* The daily seasonal factor for exit in October.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Novembre
        * *Description:* The daily seasonal factor for exit in November.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur saisonnier journalier sortie Décembre
        * *Description:* The daily seasonal factor for exit in December.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

.. _target_raccordements_pits:
.. admonition:: RaccordementsPITS
    :class: error

    *Sheet Description*: The PITS are connected to another object - Gas Account. Such account allow to have a many to one relation as one gas account can be linked to multiple pits.

    .. list-table::
        :widths: 25 25
        :header-rows: 1

        * - CompteGaz	
          - PITS
        * - Gas Account (eg: astora - Haidach | DE-NCG | Haidach)
          - PITS (eg: bayernets | DE-NCG | Haidach)

.. _raccordements_pits:

    ⚙️ CompteGaz
        * *Description:* The gas account.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ComptesGaz<target_comptes_gaz>` sheet.

    ⚙️ PITS
        * *Description:* The PITS.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`PITS<target_pits>` sheet.

.. _target_comptes_gaz:
.. admonition:: ComptesGaz
    :class: error

    *Sheet Description*: The storage are also linked to the Gas Account. Such account allow to have a many to one relation as one storage can be linked to multiple gas account.

    .. list-table::
        :widths: 25 25
        :header-rows: 1

        * - CompteGaz	
          - NomStockage
        * - Gas Account (eg: astora - Haidach | DE-NCG)
          - Storage Name (eg: astora - Haidach)

.. _comptes_gaz:

    ⚙️ CompteGaz
        * *Description:* The gas account.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`RaccordementsPITS<_target_raccordements_pits>` sheet.

    ⚙️ NomStockage
        * *Description:* The storage name.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ATS<target_ats>` sheet.

.. _target_transferts_comptes_gaz:
.. admonition:: TransfertsComptesGaz
    :class: error

    *Sheet Description*: This sheet defines the transfer between gas accounts with an assiciated cost.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - Nom	
          - Compte gaz émetteur	
          - Compte gaz récepteur	
          - Tarif de transfert [€/MWh]
        * - Name (eg: astora - Jemgum | DE-GPL>NL)
          - Gas Account Emitter (eg: astora - Jemgum | DE-GPL)
          - Gas Account Receiver (eg: astora - Jemgum | NL)
          - Transfer tariff (eg: 0.30)

.. _transferts_comptes_gaz:

    ⚙️ Nom
        * *Description:* The name of the transfer.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String.

    ⚙️ Compte gaz émetteur
        * *Description:* The gas account emitter.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ComptesGaz<target_comptes_gaz>` sheet.

    ⚙️ Compte gaz récepteur
        * *Description:* The gas account receiver.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ComptesGaz<target_comptes_gaz>` sheet.

    ⚙️ Tarif de transfert [€/MWh]
        * *Description:* The transfer tariff.
        * *Default value:* *None*
        * *Default unit:* €/MWh
        * *Validity:* Float or String. If string, it must be part of the :ref:`TarifParDate<target_tarif_par_date>` sheet.

.. _target_remplissage_stockage_final:
.. admonition:: RemplissageStockageFinal
    :class: error

    *Sheet Description*: This sheet defines the final level of the storages.

    .. list-table::
        :widths: 25 25
        :header-rows: 1

        * - Stockage
          - Niveau final [0..100]
        * - Storage (eg: astora - Haidach)
          - Final level (eg: 100) 

.. _remplissage_stockage_final:

    ⚙️ Stockage
        * *Description:* The storage.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ATS<target_ats>` sheet.

    ⚙️ Niveau final [0..100]
        * *Description:* The final level.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Integer.

.. _target_maintenance_stockage:
.. admonition:: MaintenanceStockage
    :class: error

    *Sheet Description*: This sheet defines the storage maintenance.

    .. list-table::
        :widths: 25 25 25 25 25
        :header-rows: 1

        * - NomStockage	
          - Direction	
          - Debut	
          - Fin	
          - Capa 
          - restante [MWh/j]
        * - Storage Name (eg: RAGES - RAG Storage Pool)
          - Direction (eg: Injection)
          - Start (eg: 4/8/2019)
          - End (eg: 4/14/2019)
          - Remaining capacity (eg: 193,848)

.. _maintenance_stockage:

    ⚙️ NomStockage
        * *Description:* The storage name.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ATS<target_ats>` sheet.

    ⚙️ Direction
        * *Description:* The direction.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be either "Injection" or "Withdrawal".

    ⚙️ Debut
        * *Description:* The start date.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Fin
        * *Description:* The end date.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Capa restante [MWh/j]
        * *Description:* The remaining capacity.
        * *Default value:* *None*
        * *Default unit:* MWh/d
        * *Validity:* Float.


Storage constraints used in CATS algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _target_tunnel_par_date:
.. admonition:: TunnelParDate
    :class: error

    *Sheet Description*: In Cactus, in order to refine the modelling of the storages it's possible to define ratcheting constraints. The very simplistic idea is that it's easier to fill up an empty storage than to empty a full one. Same apply for unloading a full one vs an empty one. Here the constraints defined in this sheet are not directly used in the Cactus model. The idea is that this sheet is read when building up the `cats.xml` file and then the constraints are added in the main model. 
    
    Here, this sheet is used to define the tunnel constraints for the storages. It means that we are able here to play on the min and max level of the storage.
    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - NomStockage	
          - Date	
          - Tunnel Min [0,1]	
          - Tunnel Max [0,1]
        * - Name of the storage (eg: Storengy - Serene Nord)
          - Date (eg: 4/1/2018)
          - Tunnel Min (eg: 0)
          - Tunnel Max (eg: 0.4)

.. _tunnel_par_date:

    ⚙️ NomStockage
        * *Description:* The name of the storage.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ATS<target_ats>` sheet. It can be left empty and if so the tunnel constraints will be applied to the storage define above.

    ⚙️ Date
        * *Description:* The date.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Date.

    ⚙️ Tunnel Min [0,1]
        * *Description:* The minimum tunnel.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Tunnel Max [0,1]
        * *Description:* The maximum tunnel.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

.. _target_facteurs_reduction:
.. admonition:: FacteursReduction
    :class: error

    *Sheet Description*: This sheet defines the reduction factors for the storages. This means that we are able to define a factor that will be applied to the injection or withdrawal capacity of the storage.

    .. list-table::
        :widths: 25 25 25 25
        :header-rows: 1

        * - NomStockage	
          - Direction	
          - Niveau [0,1]	
          - Facteur [0,1]
        * - Name of the storage (eg: Fluxys - Loenhout)
          - Direction (eg: Injection)
          - Level (eg: 0)
          - Factor (eg: 1)  

.. _facteurs_reduction:

    ⚙️ NomStockage
        * *Description:* The name of the storage.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be part of the :ref:`ATS<target_ats>` sheet.

    ⚙️ Direction
        * *Description:* The direction.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* String. Must be either "Injection" or "Withdrawal".

    ⚙️ Niveau [0,1]
        * *Description:* The level.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.

    ⚙️ Facteur [0,1]
        * *Description:* The factor.
        * *Default value:* *None*
        * *Default unit:* *None*
        * *Validity:* Float.