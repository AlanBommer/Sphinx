**************
Plan de tests
**************

En complément de la gestion des erreurs et du traitement des exceptions implémentés directement dans le code, un plan complet de tests a été réalisé selon la politique, l'environnement, la méthodologie et avec les participants énoncés ci-après.


Politique de tests
==================

Méthodologie :
~~~~~~~~~~~~

   Cinq type de tests sont effectués :
      - Tests fonctionnels
      - Tests de non-régression
      - Tests de robustesse
      - Tests d'endurance
      - Tests de performance

Tests fonctionnels :
~~~~~~~~~~~~~~~~~~

   **Objectif** : Valider le fonctionnement effectif de chaque module et fonction de SmartCrawl

   **Fonctionnement** :
      - Exécuter le programme avec l'ensemble des sites scénarisés du CAC40.
      - Vérifier que chaque scenario est lu
      - Vérifier que chaque scenario est exécuté
      - Vérifier que les offres d'emploi d'une même entreprise sont bien recueillies au sein d'une même archive zip
      - Vérifier que chaque archive zip correspondant à chaque entreprise est stockée dans la base de données MongoDB.

   **Résultats attendus** : Plusieurs offres d'emploi ont été téléchargées et stockées pour chaque entreprise.


Tests de Non-Régression :
~~~~~~~~~~~~~~~~~~~~~~~

   **Objectif** : Valider la non-régression

   **Fonctionnement** : Exécuter le programme avec l'ensemble des sites scénarisés du CAC40 deux semaines après le début de la période d'intrégration du client.

   **Résultats attendus** : Plusieurs offres d'emploi ont été téléchargées pour chaque site.

Tests de robustesse :
~~~~~~~~~~~~~~~~~~~

   **Objectif** : Vérifier que le programme réagit comme attendu aux erreurs de rédaction dans les scénarios

   **Fonctionnement** :
      - On rédige des scénarios pour avoir des erreurs spécifiques
      - On génère ses erreurs dans un fichier log à l'aide de l'exécution de ces scénarios
      - En paralèlle des scénarios, on rédige un fichier log de référence qui liste les erreurs attendues
      - On compare les deux fichiers log : celui de référence et celui généré par l'exécution des scénarios
      - La comparaison des deux fichiers permet de vérifier si les erreurs attendues ont bien été générées et si des erreurs non-attendues n'ont pas été générées

   **Résultat attendu** : présence de toutes les erreurs attendues et aucune erreur non-attendue

Tests d'endurance :
~~~~~~~~~~~~~~~~~

    **Objectifs** : Confirmer la capacité du programme à traiter tous les scénarios, même en cas d'erreur sur un ou plusieurs sites
    **Fonctionnement** :
      - Exécuter le programme avec l'ensemble des sites scénarisés du CAC40 et contenant des erreurs volontaires
      - Vérifier que chaque scénario est lu
      - Vérifier que chaque scénario est exécuté, même en cas d'erreur
      - Vérifier que les scénarios sans erreurs sont traités correctement
      - Vérifier que les scénarios avec erreurs volontaires sont bien recensés en erreur dans les LOGS

    **Résultat attendu** : les scénarios sans erreurs volontaires sont tous traités, jusqu'à la fin du fichier des scénarios, même si des erreurs ont eu lieu en cours d'exécution

Tests de performance :
~~~~~~~~~~~~~~~~~~~~

	**Objectifs** : Estimer le temps mis par le programme pour parcourir l'ensemble des scénarios retenus du CAC40.

	**Fonctionnement** :
	   - On lance le programme afin qu'il crawl l'ensemble des entreprises visées sur une période de 2 mois et en téléchargeant un maximum de 50 offres d'emploi par entreprise
	   - On mesure le temps total d'éxécution du programme

	**Résultat attendu** : Une durée d'exécution de la totalité des scénarios en moins de 8h (en vue d'un traitement entre 00:00 et 08:00 chaque jour.)

Domaines fonctionnels :
~~~~~~~~~~~~~~~~~~~~~~~~

	L'ensemble des actions de l'ontologie est testé.

	On vérifie ainsi la capacité du programme à :
	   - Se rendre sur tous les sites visés
	   - Trouver les offres d'emploi
	   - Les télécharger
	   - Les envoyer à la base de données

Catégorie des résultats :
~~~~~~~~~~~~~~~~~~~~~~~

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

	Les données, permettant les tests de robustesse, sont les scénarios rédigés dans le module 'Test_robustesse'.

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

	Les tests ont débuté le 13/02/2020 et se sont conclus le 26/02/2020.

	Ils se sont déroulés dans l'ordre suivant :
	   - Tests de robustesse
	   - Validation de recettes
	   - Tests d'endurance
	   - Tests de performance

	Le test de non régression sera effectué aux alentours du 28/02/2020 pendant la période d'intégration par le client.

Critères d'acceptation :
~~~~~~~~~~~~~~~~~~~~~~~~~

	Les critères d'acceptation sont :
	   - Validation de la recette : Réussite
	   - Tests de robustesse : Tolérable
	   - Test d'endurance : Réussite
	   - Test de performance : Acceptation
	   - Test de non régression : Réussite
