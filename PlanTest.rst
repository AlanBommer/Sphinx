**************
Plan de tests
**************

En complément de la gestion des erreurs et du traitement des exceptions implémentés directement dans le code, un plan complet de tests a été réalisé selon la politique, l'environnement, la méthodologie et avec les participants énoncés ci-après.


Politique de tests
==================

Méthodologie :
~~~~~~~~~~~~~~~

   Cinq type de test sont effectués :
      - Test fonctionnel
      - Test de non-régression
      - Test de robustesse
      - Test d'endurance
      - Test de performance

Test fonctionnel :
~~~~~~~~~~~~~~~~~~~~~

   **Objectif** : Valider le fonctionnement effectif de chaque module et fonction de SmartCrawl

   **Fonctionnement** :
      - Exécuter le programme avec l'ensemble des sites scénarisés du CAC40.
      - Vérifier que chaque scenario est lu et exécuté
      - Vérifier que les offres d'emploi d'une même entreprise sont bien recueillies au sein d'une même archive zip
      - Vérifier que chaque archive zip correspondant à chaque entreprise est stockée dans la base de données MongoDB.

   **Résultats attendus** : Plusieurs offres d'emploi ont été téléchargées et stockées pour chaque entreprise.

   **Résultat réalisé** :
    Temps :
    
    Erreur(s) : 0


Test de Non-Régression :
~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Objectif** : Valider la non-régression

   **Fonctionnement** : Exécuter le programme avec l'ensemble des sites scénarisés du CAC40 deux semaines après le début de la période d'intrégration du client.

   **Résultats attendus** : Plusieurs offres d'emploi ont été téléchargées et stockées pour chaque entreprise.

Test de robustesse :
~~~~~~~~~~~~~~~~~~~~~~

   **Objectif** : Vérifier que le programme réagit comme attendu aux erreurs de rédaction dans les scénarios

   **Fonctionnement** :
      - On rédige des scénarios pour avoir des erreurs spécifiques
      - On génère ses erreurs dans un fichier log à l'aide de l'exécution de ces scénarios
      - On compare les erreurs attendues et les erreurs réalisées

   **Résultat attendu** : Présence de toutes les erreurs attendues et aucune erreur non-attendue

   .. image:: IMG/TestRobustesse.jpeg
      :align: center

   **Résultat réalisé** :
    Tests réalisés : 36

    Tests réussis : 36

    Tests échoués : 0

Test d'endurance :
~~~~~~~~~~~~~~~~~~~~

    **Objectif** : Confirmer la capacité du programme à traiter tous les scénarios dans des situations différentes

    **Fonctionnement** :
    
      - Exécuter le programme en répartissant l'ensemble des scénarios sur plusieurs requêtes possédant des paramètres différents (contrainte sur la date, le navigateur ou le maxJobs)
      - Vérifier que chaque scénario est lu

    **Résultat attendu** : Aucune erreur générée par le test.

    **Résultat réalisé** :

    .. image:: IMG/ResultEndu.png
      :align: center

Test de performance :
~~~~~~~~~~~~~~~~~~~~~~~

  **Objectif** : Estimer le temps mis par le programme pour parcourir l'ensemble des scénarios retenus du CAC40.

  **Fonctionnement** :
     - On lance le programme afin qu'il crawl l'ensemble des entreprises visées sur une période de 2 mois et en téléchargeant un maximum de 50 offres d'emploi par entreprise
     - On mesure le temps total d'éxécution du programme

  **Résultat attendu** : Une durée d'exécution de la totalité des scénarios en moins de 8h (en vue d'un traitement entre 00:00 et 08:00 chaque jour.)

  **Résultat réalisé** :
    Temps :

    Erreur(s) :

Domaines fonctionnels :
~~~~~~~~~~~~~~~~~~~~~~~~

  L'ensemble des actions de l'ontologie est testé.

  On vérifie ainsi la capacité du programme à :
     - Se rendre sur tous les sites visés
     - Trouver les offres d'emploi
     - Les télécharger
     - Les envoyer à la base de données

Catégorie des résultats :
~~~~~~~~~~~~~~~~~~~~~~~~~~

   Réussite : conformité aux attentes

   Acceptation : résultat observé diffère des spécifications mais reste acceptable

   Tolérance : résultat incorrect mais reste exploitable

   Inadmissibilité : résultat incorrect devant être corrigé

Environnement de test
======================

Matériels :
~~~~~~~~~~~~

   Les tests ont été effectués sur les machines mises à la disposition des développeurs par l'Ecole Centrale Supélec dans le cadre du Mastère SIO.

Données de test :
~~~~~~~~~~~~~~~~~~

  Les données permettant les tests sont les scénarios rédigés dans le dossier 'SCN_test'

  Les données, permettant les tests d'endurance et de performances, sont les scénarios des entreprises du CAC40.

Attribution des participants
=============================

Testeurs :
~~~~~~~~~~~

  Les tests ont été réalisés par : JOUBIOUX Alan et SCAËROU Nicolas

Chef de test :
~~~~~~~~~~~~~~~

  Les tests ont été supervisés par : FABRE Nicolas

Modes de Tests
===============

Planning :
~~~~~~~~~~~

  Les tests ont débuté le 13/02/2020 et se sont conclus le 28/02/2020.

  Ils se sont déroulés dans l'ordre suivant :
     - Test de robustesse
     - Validation de recettes
     - Test d'endurance
     - Test de performance

  Le test de non régression sera effectué aux alentours du 18/03/2020 pendant la période d'intégration par le client.

Critères d'acceptation :
~~~~~~~~~~~~~~~~~~~~~~~~~

  Les critères d'acceptation sont :
     - Validation de la recette : Réussite
     - Test de robustesse : Tolérable
     - Test d'endurance : Réussite
     - Test de performance : Acceptation
     - Test de non régression : Réussite
