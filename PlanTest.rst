**************
Plan de tests
**************

Politique de test
==================

Méthodologie :
~~~~~~~~~~~~~~~

   Cinq tests sont effectués :
      - Test fonctionnel
      - Test de non-régression
      - Test de robustesse
      - Test d'endurance
      - Test de performance

Test fonctionnel :
~~~~~~~~~~~~~~~~~~~

   **Objectif** : Valider la recette

   **Fonctionnement** : Exécuter le programme avec l'ensemble des sites scénarisés du CAC40.

   **Résultat attendu** : Plusieurs offres d'emploi ont été téléchargées pour chaque site.


Test de Non-Régression :
~~~~~~~~~~~~~~~~~~~~~~~~~

   **Objectifs** : Valider la non-régression

   **Fonctionnement** : Exécuter le programme avec l'ensemble des sites scénarisés du CAC40 deux semaines après le début de la période d'intrégration du client.

   **Résultat attendu** : Plusieurs offres d'emploi ont été téléchargées pour chaque site.

Test de robustesse :
~~~~~~~~~~~~~~~~~~

   **Objectifs** : Vérifier que le programme réagit comme attendu aux erreurs de rédaction dans les scénarios

   **Fonctionnement** :
      - On rédige des scénarios pour avoir des erreurs spécifiques
      - On génère ses erreurs dans un fichier log à l'aide de l'exécution de ces scénarios
      - En paralèlle des scénarios, on rédige un fichier log de référence qui liste les erreurs attendues
      - On compare les deux fichiers log : celui de référence et celui généré par l'exécution des scénarios
      - La comparaison des deux fichiers nous permet de vérifier si les erreurs attendues ont bien été générées et si des erreurs non-attendues n'ont pas été générées

   **Résultat attendu** : présence de toutes les erreurs attendues et aucune erreur non-attendue

Test d'endurance :
~~~~~~~~~~~~~~~~~

    **Objectifs** : Confirmer la capacité du programme à s'adapter aux différents sites visés.

    **Fonctionnement** :
       - 
       -

    **Résultat attendu** :

Test de performance :
~~~~~~~~~~~~~~~~~~~

	**Objectifs** : Estimer le temps mis par le programme pour parcourir l'ensemble des scénarios retenus du CAC40.

	**Fonctionnement** :
	   - On lance le programme afin qu'il crawl l'ensemble des entreprises visées sur une période de 2 mois et en téléchargeant un maximum de 50 offres d'emploi
	   - On mesure le temps total d'éxécution du programme

	**Résultat attendu** :  un temps d'éxécution permettant en production une exécution durant la nuit.

Domaines fonctionnels :
~~~~~~~~~~~~~~~~~~~~~~~~

	L'ensemble des actions de l'ontologie sont testés.

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

   Les tests ont été effectués sur les machines mises à la disposition des développeurs par l'Ecole Centrale Supélec dans le cadre du Master SIO.

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

	Le test de non régression sera effectuée aux alentours du 12/02/2020 pendant la période d'intégration par le client.

Critères d'acceptation :
~~~~~~~~~~~~~~~~~~~~~~~~~

	Les critères d'acceptation sont :
	   - Validation de la recette : Réussite
	   - Tests de robustesse : Tolérable
	   - Test d'endurance : Réussite
	   - Test de performance : Acceptation
	   - Test de non régression : Réussite