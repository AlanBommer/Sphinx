**************************************************************************
Présentation des blocs permettant l'écriture des scénarios du SMART PATH
**************************************************************************

Préliminaire :
===============
 * L'écriture des scénarios s'effectue au format YAML.
 * Une liste YAML correspond à un scénario de site.
 * Une liste YAML est rédigée pour chaque site dans un fichier commun '*scenarii.yaml*'
 * Il est possible de tester les scénarios sur le site : 'http://www.yamllint.com/'
 * Un exemple de fichier '*scenarii.yaml*' se trouve à la fin de ce document.

.. topic:: Liste des blocs

   #. GoPage()
   #. ClickPage()
   #. SaveJob()
   #. Scroll()
   #. GoBack()
   #. FindDate()

.. topic:: Gestion des nodes

   1. La première ligne du scénario renvoie au nom du site traité.
   2. La seconde ligne du scénario renvoie au premier node du scénario, indexé '0'
   3. Typologie des nodes :

      * *actualNode* = node de la ligne traitée
      * *nextNode* = repère pour envoyer à un autre node à la fin du bloc, par défaut 'nextNode' renvoie au node de la ligne suivante
      * *possibleNode* = repère pour envoyer à un node si une condition interne au bloc est validée
   4. En cas de problème lors de l'exécution du bloc, le 'possibleNode' référencé sera le node utilisé par défaut pour poursuivre le scénario.
   5. En cas de problème lors de l exécution de la dernière ligne du scénario et en l'absence d'un 'possibleNode', le scénario s'arrête.

   .. warning:: Attention aux éventuelles boucles infinies avec la gestion des nodes.

.. topic:: Gestion des tags

   #. Un tag est défini selon deux paramètres.
   #. '*class*', '*name*', '*target*'' sont les types de balises recherchées
   #. Les types de balises sont liées à une chaine de caractère
   #. En cas de recherche dans des balises en cascade, les tags sont imbriqués dans un dictionnaire
   #. En cas de recherche dans une balise d un niveau équivalent, on utilisera "index : n" pour renvoyer à la balise \ *n*\ -suivante

Description des blocs :
========================


Bloc GoPage() :
++++++++++++++++
	Le bloc **GoPage()** permet d accéder à la page web des offres.
	Il nécessite en entrée un lien internet qui renvoie à la page d offre d emplois de l entreprise visée.

.. topic:: Exemple : 

   .. code-block:: YAML 
      
      GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}

      GoPage : référence du bloc utilisé
      'url' : variable d'entrée du bloc
      'https://www.safran-group.com/fr/emplois?pays=France' : adresse url renvoyant à la page web du site d offre d emplois

Bloc ClickPage()
+++++++++++++++++
	Le bloc **ClickPage()** permet de cliquer sur un lien url spécifique : fonction recherche, accéder à l'offre d'emploi, accéder à la page suivante du site.
	Il nécessite en entrée la liste des tags nécessaires à la navigation dans la page HTML.

.. topic:: Exemple :
   
   .. code-block:: YAML 

      ClickPage: {'tag' : {'class' : 'type type-28 viewport', 'tag' : {'name' : 'a'}}, 'possibleNode' : 5}

      ClickPage : référence du bloc utilisé
      'tag' : marqueur lié à la recherche HTML
      'class' : type du tag recherché
      'type type-28 viewport' : valeur de la variable 'class'
      'tag' : marqueur lié à la recherche HTML
      'name' : type du tag recherché
      'a' : valeur de la variable 'name'

   **Note** : Ici on remarque l'utilisation en cascade des tags permettant de trouver l'adresse html nécessaire à la poursuite du scénario et l'appel au node 5 en cas d échec dans la recherche des tags.

Bloc SaveJob()
+++++++++++++++
        Le bloc **SaveJob()** permet de sauvegarder l'offre d'emploi.
	Il ne nécessite pas de variable d'entrée. Le programme python est chargé d'effectuer la sauvegarde locale puis le transfert sur la base de donnée.

.. topic:: Exemple :

   .. code-block:: YAML 

      SaveJob: {}

      SaveJob : référence du bloc utilisé

Bloc Scroll()
++++++++++++++
	Le bloc **Scroll()** permet de simuler l'action de la souris afin de charger les données dynamiques du site.
	Il nécessite en entrée un entier int relatif à la distance nécessaire pour afficher les nouvelles informations.

.. topic:: Exemple :

   .. code-block:: YAML 

      Scroll : {'size' : 10, 'possibleNode' : 5}

      Scroll : référence du bloc utilisé
      'size : 10' : paramètrage de la taille du scroll nécéssaire.
      'possibleNode : 5' : en cas d'absence de chargement de donnée, on se rend au node 5, si aucune variable n'est renseignée et en cas d'absence de chargement de donnée, le scénario s'arrête

Bloc GoBack()
++++++++++++++
	Le bloc **GoBack()** permet d'effectuer un retour en arrière pour retourner sur la page url précédente.
	Il nécessite en entrée la valeur du 'nextNode'.

.. topic:: Exemple :

   .. code-block:: YAML 
      
      GoBack: {'nextNode' : 2}

      GoBack : référence du bloc utilisé
      'nextNode : 2' : paramètrage du node appellé à la suite

Bloc FindDate()
++++++++++++++++
	Le bloc **FindDate()** permet de repérer la date présente dans la page. En interne, il déterminera si l'offre d'emploi est intéressante ou non.
	Il nécessite en entrée la liste des tags nécessaires à la navigation dans la page HTML.

.. topic:: Exemple :
   
   .. code-block:: YAML 

      FindDate: {'tag' : {'class' : 'ts-offer-card-content offerContent', 'tag' : {'name' : 'li', 'index' : 1 }}}

      FindDate : référence du bloc utilisé
      'tag' : marqueur lié à la recherche HTML
      'class' : type du tag recherché
      'ts-offer-card-content offerContent' : valeur de la variable 'class'
      'tag' : marqueur lié à la recherche HTML
      'name' : type du tag recherché
      'li' : valeur de la variable 'name'
      'index : 1' : marqueur et valeur lié à la recherche dans la balise soeur n°1

   **Note** : Exemple ici de l'utilisation de l'index pour la recherche d'une balise au même niveau que la précédente.

Récapitulatif des blocs généralisés :
======================================

.. code-block:: YAML 

   - NomSite:
      - GoPage: {'url': "url_site"}   # Je vais sur la page emploi
         - Scroll: {'size' : int, 'possibleNode' : int} # Je scroll pour charger la page, en cas d'échec je vais au node référencé
         - FindDate: {'tag' : {'class' : str, 'tag' : {'name' : str, 'index' : int }}} # Je cherche la balise permettant de trouver la date de la première offre, avec deux tags père-fils et 'N' tag frère
         - ClickPage: {'tag' : {'class' : str, 'tag' : {'target' : str}}, 'possibleNode' : int} # Je clique sur le lien de l'offre d'emploi, en cas de problème je me rend au node référencé
         - SaveJob: # Je sauvegarde l offre
         - GoBack: {'nextNode' : int} #Je reviens en arrière et lance le bloc du node référencé
         - ClickPage: {'tag' : {'class' : str}, 'nextNode' : int, 'possibleNode' : int} # Je clique sur le lien permettant de continuer la recherche d'emploi et lance l'un des deux blocs des nodes référencés*

Exemples de scénarios :
========================

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
