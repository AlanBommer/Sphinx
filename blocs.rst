*********************
Ontologie SmartCrawl
*********************

Introduction :
===============

Le programme 'SmartCrawl' s'insère au début du processus du 'SmartPath'. Il a pour objectif de parcourir les sites d'entreprises afin de récupérer les offres d'emploi.
A cet effet, 'SmartCrawl' "visite" les sites listés et "lit" les offres d'emploi, sauvegarde celles qui l'intéresse avant de les transmettre à la base de donnée permettant ensuite à 'SmartPath' de les traiter.
Pour permettre à 'SmartCrawl' de visiter les sites, l'opérateur doit lui fournir les 'scénarios' des sites web.

Un scénario est rédigé par site web. Les scénarios sont écrits au format YAML et sont regroupés dans un même fichier '*scenarii.yaml*'. Un exemple se trouve à la fin du présent document.
Un scénario est une liste d'actions rédigées au format YAML.

Les actions sont celles qu'auraient dû faire un utilisateur humain pour parcourir les offres d'emploi. Par conséquent, la visite et l'étude des sites web est nécessaire afin de rédiger les scénarios. Elles ont besoin pour fonctionner de différents paramètres d'entrée.

Préambule technique :
======================

.. topic:: Liste des actions

   Les actions sont au nombre de 6 et elles permettent d'avoir un impact déterminé sur la page web.

   #. GoPage, pour se rendre sur une page donnée
   #. ClickPage, pour clicker sur un lien donné
   #. SaveJob, pour sauvegarder l'emploi
   #. Scroll, pour faire dérouler la page actuelle
   #. GoBack, pour revenir en arrière
   #. FindDate, pour chercher la date des offres d'emploi dans la page actuelle

.. topic:: Gestion des nodes

   Un node est un point de repère permettant au programme de naviguer au sein d'un scénario et de renvoyer à différentes lignes du scénario.
   Les conventions suivantes permettent la rédaction d'un scénario cohérent.

   1. La première action du scénario renvoie au premier node du scénario, indexé '0'
   2. Les nodes sont rentrés en paramètres dans les actions.
   3. Les nodes possèdent trois états différents :

      * *actualNode* = node de l'action actuelle, il n'est jamais exprimé.
      * *nextNode* = node qui sera traité à la fin de l'action, par défaut 'nextNode' renvoie au node de l'action suivante'
      * *possibleNode* = node qui sera appelé si certaines conditions sont réunies lors l'exécution de l'action actuelle.
   4. En cas d'erreur lors de l'exécution, si un 'possibleNode' est paramétré alors il sera utilisé par défaut pour poursuivre le scénario.
   5. En cas d'erreur lors de l'exécution, si un 'nextNode' est paramétré, et qu'il n'y a aucun 'possibleNode', alors il sera utilisé par défaut pour poursuivre le scénario.
   6. En cas d'erreur lors de l'exécution et en cas d'absence de paramétrage de node, alors la ligne suivante du scénario sera exécutée.

.. topic:: Gestion des tags

   #. Un tag est défini selon deux paramètres. # Préciser
   #. '*class*', '*name*', '*target*'' sont les types de balises recherchées
   #. Les types de balises sont liés à une chaine de caractères
   #. En cas de recherche dans des balises en cascade, les tags sont imbriqués dans un dictionnaire
   #. En cas de recherche dans une balise d un niveau équivalent, on utilisera "index : n" pour renvoyer à la balise \ *n*\ -suivante

Description des actions :
=========================

Action GoPage :
++++++++++++++++

.. topic:: Présentation :

   L'action **GoPage** permet d accéder à la page web des offres.
	 Il nécessite en entrée un lien internet qui renvoie à la page d offre d emplois de l entreprise visée.

   Paramètres :

      * 'url' : variable principale de l'action, valeur : adresse url renvoyant à la page web du site d'offre d'emplois.

.. topic:: Exemple :

   .. code-block:: YAML 
      
      GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}

Action ClickPage
+++++++++++++++++

.. topic:: Présentation :

	L'action **ClickPage** permet de cliquer sur un lien url spécifique : fonction recherche, accéder à l'offre d'emploi, accéder à la page suivante du site.
	Il nécessite en entrée le chemin nécessaire à la navigation dans la page HTML.

  Paramètres :

     * 'path' : variable principale de l'action, valeur : XPATH des balises HTML

.. topic:: Exemple :
   
   .. code-block:: YAML 

      ClickPage: {'path' : /html/body/div[2]/div[2]/div[1]/div[4]/div/div[2]/ul[2]/li[13]/a, 'nextNode' : 1}
      ClickPage: {'tag' : {'class' : 'type type-28 viewport', 'tag' : {'name' : 'a'}}, 'possibleNode' : 5}

      ClickPage : référence de l'action utilisée
      'tag' : marqueur lié à la recherche HTML
      'class' : type du tag recherché
      'type type-28 viewport' : valeur de la variable 'class'
      'tag' : marqueur lié à la recherche HTML
      'name' : type du tag recherché
      'a' : valeur de la variable 'name'

   **Note** : Ici on remarque l'utilisation en cascade des tags permettant de trouver l'adresse html nécessaire à la poursuite du scénario et l'appel au node 5 en cas d échec dans la recherche des tags.

Action SaveJob
+++++++++++++++

.. topic:: Présentation :

  L'action **SaveJob** permet de sauvegarder l'offre d'emploi.
	Il ne nécessite pas de paramètre. Le programme est chargé d'effectuer la sauvegarde locale puis le transfert sur la base de donnée.

.. topic:: Exemple :

   .. code-block:: YAML 

      SaveJob: {}

Action Scroll
++++++++++++++

.. topic:: Présentation :

	L'action **Scroll** permet de simuler l'action de la souris afin de charger les données dynamiques du site.
	Il nécessite en entrée un entier int relatif à la distance nécessaire pour afficher les nouvelles informations.

  Paramètres :

     * 'size' : variable principale de l'action, valeur : taille du scroll nécessaire.

.. topic:: Exemple :

   .. code-block:: YAML 

      Scroll : {'size' : 10, 'possibleNode' : 5}

Action GoBack
++++++++++++++

.. topic:: Présentation :

	L'action **GoBack** permet d'effectuer un retour en arrière pour retourner sur la page url précédente.
	Il nécessite en entrée le renvoi sur l'action à exécuter à l'issue

  Paramètres :

     * 'nextNode' : valeur principale de l'action, valeur : node de l'action à exécuter à l'issue.

.. topic:: Exemple :

   .. code-block:: YAML 
      
      GoBack: {'nextNode' : 2}

Action FindDate
++++++++++++++++

.. topic:: Présentation :

	L'action **FindDate** permet de repérer la date présente dans la page. En interne, il déterminera si l'offre d'emploi est intéressante ou non (*i.e* si les offres d'emploi ont été publiées après une date pré-déterminée)
	Il nécessite en entrée le chemin nécessaire à la navigation dans la page HTML.

  Paramètres :

     * 'path' : variable principale de l'action, valeur : XPATH des balises HTML

.. topic:: Exemple :
   
   .. code-block:: YAML 

      FindDate: {'tag' : /html/body/div[2]/div[2]/div[1]/div[4]/div/div[2]/ul[1]/li[1]/a/div[2]/span, 'possibleNode' : 5}
      FindDate: {'tag' : {'class' : 'ts-offer-card-content offerContent', 'tag' : {'name' : 'li', 'index' : 1 }}}

      FindDate : référence de l'action utilisée
      'tag' : marqueur lié à la recherche HTML
      'class' : type du tag recherché
      'ts-offer-card-content offerContent' : valeur de la variable 'class'
      'tag' : marqueur lié à la recherche HTML
      'name' : type du tag recherché
      'li' : valeur de la variable 'name'
      'index : 1' : marqueur et valeur lié à la recherche dans la balise soeur n°1

   **Note** : Exemple ici de l'utilisation de l'index pour la recherche d'une balise au même niveau que la précédente.

Récapitulatif des actions généralisées :
========================================

.. code-block:: YAML 

   - NomSite:
      - GoPage: {'url': "url_site"}   # Je vais sur la page emploi
         - Scroll: {'size' : int, 'possibleNode' : int} # Je scroll pour charger la page, en cas d'échec je vais au node référencé
         - FindDate: {'tag' : {'class' : str, 'tag' : {'name' : str, 'index' : int }}} # Je cherche la balise permettant de trouver la date de la première offre, avec deux tags père-fils et 'N' tag frère
         - ClickPage: {'tag' : {'class' : str, 'tag' : {'target' : str}}, 'possibleNode' : int} # Je clique sur le lien de l'offre d'emploi, en cas de problème je me rend au node référencé
         - SaveJob: # Je sauvegarde l offre
         - GoBack: {'nextNode' : int} #Je reviens en arrière et lance le action du node référencé
         - ClickPage: {'tag' : {'class' : str}, 'nextNode' : int, 'possibleNode' : int} # Je clique sur le lien permettant de continuer la recherche d'emploi et lance l'un des deux actions des nodes référencés*

Recommandations :
=================

   .. warning::

      * Des boucles infinies peuvent être créées lors de la rédaction des 'possibleNode'
      * Il est recommander de vérifier la synthaxe des scénarios sur le site : 'http://www.yamllint.com/'


Exemples de scénarios / fichier '*scenarii.yaml*'
==================================================

.. topic:: SAFRAN

   .. code-block:: YAML

      - SAFRAN:
        - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}
        - FindDate: {'tag' : {'class' : 'date'}, 'possibleNode' : 5}
        - ClickPage: {'tag' : {'class' : 'offer-card'}}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : {'class' : 'next', 'tag' : {'name' : 'a'}}, 'nextNode' : 1}

.. topic:: BNP

   .. code-block:: YAML 

      - BNP:
        - GoPage: {'url': "https://group.bnpparibas/emploi-carriere/toutes-offres-emploi/france"}
        - Scroll: {'size' : 10, 'possibleNode' : 5}
        - ClickPage: {'tag' : {'class' : 'type type-28 viewport', 'tag' : {'name' : 'a'}}, 'possibleNode' : 5}
        - SaveJob:        
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : {'class' : 'progress-buton elastic show-more'}, 'nextNode' : 1, 'possibleNode' : 6}
        - ClickPage: {'tag' : {'class' : 'next', 'tag' : {'name' : 'a'}, 'nextNode' : 1}}

.. topic:: SODEXO

   .. code-block:: YAML

      - SODEXO:
        - GoPage: {'url': "https://fr.sodexo.com/home/nous-rejoindre/rejoignez-nos-equipes.html"}
        - FindDate: {'tag' : {'class' : 'ts-offer-card-content offerContent', 'tag' : {'name' : 'li', 'index' : 1 }}}
        - ClickPage: {'tag' : {'class' : 'ts-offer-card__title'}}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : {'class' : 'ts-ol-pagination-list-item__link ts-ol-pagination-list-item__link--next'}, 'nextNode' : 1}

.. topic:: TOTAL

   .. code-block:: YAML

      - TOTAL:
        - GoPage: {'url' : 'https://krb-sjobs.brassring.com/tgnewui/search/home/home?partnerid=30080&siteid=6559#Pays=France&keyWordSearch='}
        - ClickPage: {'tag' : {'class' : 'primaryButton ladda-button ng-binding'}}
        - FindDate: {'tag' : {'class' : 'jobProperty position1'}}
        - ClickPage: {'tag' : {'class' : 'jobProperty jobtitle'}}
        - SaveJob:        
        - GoBack: {'nextNode' : 2}
        - ClickPage: {'tag' : {'class' : 'showMoreJobs UnderLineLink ng-binding'}, 'nextNode' : 2}

.. topic:: CANAL

   .. code-block:: YAML

      - CANAL:
        - GoPage: {'url' : 'https://www.vousmeritezcanalplus.com/metiers.html'}
        - FindDate: {'tag' : {'class' : 'srJobListPublishedSince'}}
        - ClickPage: {'tag' : {'class' : 'srJobListJobOdd'}}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
 
.. topic:: DASSAULT

   .. code-block:: YAML

      - DASSAULT:
        - GoPage : {'url' : 'https://careers.3ds.com/fr/jobs?woc=%7B%22pays%22%3A%5B%22pays%2Ffrance%22%5D%7D'}
        - ClickPage : {'tag' : {'class' : 'ds-card ds-card--lines ds-card--image ', 'tag' : {'target' : ''}}, 'possibleNode' : 4}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : {'class' : 'ds-pagination__next', 'tag' : {'name' : 'a'}, 'nextNode' : 1}}

.. topic:: SAFRAN_XPATH

   .. code-block:: YAML

      - SAFRAN_XPATH:
        - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}
        - FindDate: {'tag' : /html/body/div[2]/div[2]/div[1]/div[4]/div/div[2]/ul[1]/li[1]/a/div[2]/span, 'possibleNode' : 5}
        - ClickPage: {'tag' : /html/body/div[2]/div[2]/div[1]/div[4]/div/div[2]/ul[1]/li[1]/a}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : /html/body/div[2]/div[2]/div[1]/div[4]/div/div[2]/ul[2]/li[13]/a, 'nextNode' : 1}
