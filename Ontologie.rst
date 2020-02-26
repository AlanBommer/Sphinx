************************
Rédaction des scénarios
************************


Introduction
=============

Le programme 'SmartCrawl' s'insère au début du processus du 'SmartPath'. Il a pour objectif de parcourir les sites d'entreprises afin de récupérer les offres d'emploi.
A cet effet, 'SmartCrawl' "visite" les sites listés et "lit" les offres d'emploi, sauvegarde celles qui l'intéresse avant de les transmettre à la base de donnée permettant ensuite à 'SmartPath' de les traiter.
Pour permettre à 'SmartCrawl' de visiter les sites, l'opérateur doit lui fournir les 'scénarios' des sites web.

Un scénario est rédigé par site web. Les scénarios sont écrits au format YAML et sont regroupés dans un même fichier '*scenarii.yaml*'. Un exemple se trouve à la fin du présent document.
Un scénario est une liste d'actions rédigées au format YAML. 

Les actions sont celles qu'auraient dû faire un utilisateur humain pour parcourir les offres d'emploi. Par conséquent, la visite et l'étude des sites web est nécessaire afin de rédiger les scénarios. Elles ont besoin pour fonctionner de différents paramètres d'entrée.

Préambule technique
=====================

Liste des actions :
~~~~~~~~~~~~~~~~~~~~

   Les actions sont au nombre de 8 et elles permettent d'avoir un impact déterminé sur la page web.

   #. GoPage, pour se rendre sur une page donnée
   #. ClickPage, pour clicker sur un lien donné
   #. GoNewTab, pour ouvrir dans un nouvel onglet un lien donné
   #. SaveJob, pour enregistrer la page HTML de l'emploi
   #. Scroll, pour faire dérouler la page actuelle
   #. GoBack, pour revenir en arrière
   #. CloseTab, pour fermer un onglet précédemment ouvert
   #. FindDate, pour chercher la date des offres d'emploi dans la page actuelle

Gestion des actions :
~~~~~~~~~~~~~~~~~~~~~~

   1. Un scénario comprend plusieurs actions. La première action du scénario est indexée '0'
   2. Il existe deux clés permettant d'exprimer quelle est la prochaine action à exécuter. L'utilisation de ces clés permet de créer des boucles et de parcourir tout le site internet.
   3. Les clés suivantes permettent de définir la prochaine action à exécuter : 

      * *nextAction* = action qui sera traitée à la fin de l'action actuelle si elle s'éxécute correctement, par défaut 'nextAction' renvoie à l'action de la ligne suivante du scénario
      * *possibleAction* = action qui sera appelée si l'action actuelle ne remplit pas son objectif *(ex : si l'action "FindDate" ne trouve pas de date ou si l'action "ClickPage" ne trouve pas de bouton 'Page suivante' )*

   4. La valeur des paramètres 'nextAction' et 'possibleAction' est de type **int** et est définit par l'index dans le scénario de l'action à appeller. 
   5. Cas particulier. En cas d'erreur lors de l'exécution, s'il n'y a aucun 'possibleAction', alors le scénario s'arrête.

   .. code-block:: YAML

      - Exemple:
            - GoPage: {'url' : 'www.example.com'} # Je me rend sur le site example.com
            - Exemple1: {'possibleAction' : 3} # Si Exemple1 fonctionne, j'exécute Exemple2. Sinon j'exécute Exemple3
            - Exemple2: { ... } # J'exécute Exemple2 et dans tous les cas, j'exécute ensuite Exemple3
            - Exemple3: {'nextAction' : 1} # Si Exemple3 fonctionne, j'exécute Exemple1. Sinon, je sors du scénario

.. _Gestiontags:

Gestion des tags :
~~~~~~~~~~~~~~~~~~~

  1. Le programme s'appuie sur les élements du dom HTML pour scrapper les données. Nous les appellerons des tags.
  2. Les tags sont définis selon le modèle 'XPATH'. Vous trouverez un tutoriel complet sur la rédaction des xpath au lien suivant : 'https://www.guru99.com/xpath-selenium.html'
  3. Vous trouverez ci-dessous plusieurs types de xpath utilisés :

     .. code-block:: YAML

      - Exemple:
        - Exemple: {'xpath' : '//div[@class="topcard"]//div//p//span'}
        - Exemple: {'xpath' : '//div[@class="container"]//div//div//div/child::div[4]/child::span[2]//strong'}
        - Exemple: {'xpath' : '//input[@id="ctl00_ContentPlaceHolder1_BtnApply"]'}
        - Exemple: {'xpath' : '//tr[contains(@class,"Greycell")]//td//a'}
        - Exemple: {'xpath' : '//ul[@class="list")]/li/a'}
        - Exemple: {'xpath' : '//div[@id="job_results_list_hldr"]//div[starts-with(@id,"job_list")]//div[@class="jlr_title"]//p//a'}

  8. La recherche des tags ne peut s'effectuer qu'au travers des actions "FindDate", "ClickPage", "GoNewTab", "CloseTab". Pour "FindDate", le programme cherchera une valeur textuelle au format d'une date. Pour les autres actions, le programme cherchera une url.

.. note:: 1. Via cette gestion des tags, il est possible d'arriver rapidement à la donnée voulue. Pour cela, il est conseillé de déterminer la valeur d'un xpath unique. Il est conseillé de tester son xpath via l'inspecteur de page HTML du navigateur Web.
     2. Il est préférable définir les valeurs des attributs dans la page HTML qui ne sont pas susceptibles d'être modifiés.

Gestion des index :
~~~~~~~~~~~~~~~~~~~

  1. Afin de naviguer entre les différentes offres d'emploi, le programme a besoin de poser des points de repères pour ensuite jalonner son trajet.

  2. Il faut rajouter la clé 'persistentIndex' dans le paramétrage des actions "Scroll", "GoNewTab", ClickPage" ou "FindDate" pour créer ces points de repère. Ainsi, le programme peut naviguer d'action en action en connaissant les balises déjà visitées.

  3. En rajoutant la clé 'persistentIndex' dans les actions, le programme pourra itérer sur les offres d’emploi d’une page. L'itération être réalisée pour les jobs, les dates et le scroll. Le programme s'adaptera automatiquement. Si vous précisez pas la clé, il ne prendra en compte que le 1er élément. 

   .. code-block:: YAML

      - EXEMPLE:
           - GoPage: {'url': "https://www.exemplesiteemplois.com/fr"} 
           - ClickPage: {'xpath' : 'XPATH'} # Action permettant d'accéder aux offres d'emploi
           - FindDate: {'xpath' : 'XPATH', 'persistentIndex', 'possibleAction' : 5} # J'indexe l'action liée à la recherche de date
           - ClickPage: {'xpath' : 'XPATH', 'persistentIndex'} # J'indexe l'action liée à mon emploi.
           - SaveJob:
           - ...

  4. Si l'on est déjà sur la page du job et que l'on recherche seulement la date de publication, la clé 'persistentIndex' n'est pas utile.

  5. La réinitialisation de l'index persistant se fait dans le paramétrage d'une action. On utilise la clé 'resetIndex' et une valeur 'liste[int]' relative au numéro de l'action dans laquelle le marqueur a été initialisé.

   .. code-block:: YAML

      - EXEMPLE:
           - GoPage: {'url': "https://www.exemplesiteemplois.com/fr"} 
           - ClickPage: {'xpath' : 'XPATH'} # Action permettant d'accéder aux offres d'emploi
           - GoNewTab: {'xpath' : 'XPATH', 'persistentIndex'} # J'indexe l'action liée à mon emploi.
           - FindDate: {'xpath' : 'XPATH'} # Etant déjà sur la page d'emploi, il n'est pas utile d'indexé l'action.
           - SaveJob: {}
           - CloseTab: {'nextAction' : 1} # Je reviens à l'action 1 et repère la balise déjà visitée grâce au marqueur déposé
           - ClickPage: {'xpath' : 'XPATH', 'resetIndex' : [2], 'nextAction' : 1} # Remise à zéro du marqueur défini dans l'action 3 : "GoNewTab" lorsque le scénario se rendra sur la page suivante du site.

Description des actions
========================

Action GoPage :
~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **GoPage** permet d'accéder à la page web des offres. Il nécessite en entrée un lien internet qui renvoie à la page des offres d'emplois de l'entreprise visée.

   Paramètre :

      * 'url' : variable principale de l'action. Valeur : adresse url renvoyant à la page web des offres d'emplois.

.. code-block:: YAML

   - EXEMPLE:
      - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}

Action ClickPage :
~~~~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **ClickPage** permet de cliquer sur un lien url spécifique : fonction recherche, accéder à l'offre d'emploi, accéder à la page suivante du site. Il nécessite en entrée le chemin nécessaire à la navigation dans la page HTML.

   Paramètre :

      * 'xpath' : variable principale de l'action. Valeur : chemin xpath de l'adresse ciblée (voir :ref:`Gestiontags`)

.. code-block:: YAML

   - EXEMPLE:
      - ClickPage: {'xpath' : '//ul[@class="list")]/li/a', 'persistentIndex'}

Action GoBack :
~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **GoBack** permet d'effectuer un retour en arrière pour retourner sur la page url précédente. Il nécessite en entrée le renvoi sur l'action à exécuter à l'issue

   Paramètre :

      * 'nextAction' : variable principale de l'action. Valeur : index de l'action à exécuter à l'issue, type *int*.

.. code-block:: YAML

   - EXEMPLE:
      - GoBack: {'nextAction' : 2}

Action GoNewTab :
~~~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **GoNewTab** possède les même caractéristiques que l'action **ClickPage**. La différence vient de l'ouverture d'un onglet pour continuer la navigation.

   Paramètre :

      * 'xpath' : variable principale de l'action. Valeur : chemin xpath de l'adresse ciblée (voir :ref:`Gestiontags`)

.. note:: Il est conseillé d'utiliser cette action pour ouvrir une offre d'emploi, cela permet de passer outre certains blocages de sites. Cette action devra être couplée à l'action **CloseTab** en aval dans le scénario.



.. code-block:: YAML

   - EXEMPLE:
      - GoNewTab: {'xpath' : '//ul[@class="list")]/li/a', 'persistentIndex'}


Action CloseTab :
~~~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **CloseTab** possède les même caractéristiques que l'action **CloseTab**. La différence permet la fermeture d'un onglet préalablement ouvert via l'action ****GoNewTab**.

   Paramètre :

      * 'nextAction' : variable principale de l'action. Valeur : index de l'action à exécuter à l'issue, type *int*.

.. note:: Cette action devra être couplée à l'action **GoNewTab** en amont dans le scénario. Ne pas oublier le paramètre 'nextAction', en effet dans le cas contraire, la prochaine action à être appellée le sera dans un onglet fermé et ne pourra pas s'exécuter.


.. code-block:: YAML

   - EXEMPLE:
      - CloseTab: {'nextAction' : 2}

Action SaveJob :
~~~~~~~~~~~~~~~~~

.. topic:: Présentation :

    L'action **SaveJob** permet de sauvegarder la page HTML de l'offre d'emploi. Le programme est chargé d'effectuer la sauvegarde locale puis le transfert sur la base de donnée.


    Il peut prendre en entrée le paramètre 'maxJobs' de type **int**. Ce paramètre permet de spécifier le nombre d'emplois télécharger. Si le paramètre n'est pas renseigné. Par défaut, aucune limitation n'est fixée.

    Paramètre :

      * 'maxJobs' : variable principale de l'action. Valeur : nombre de jobs à enregistrer, type *int*.

.. note:: Il est possible de spécifier dans le terminal une valeur de 'maxJobs' pour l'ensemble des scénarios. Un 'maxJobs' renseigné dans un scénario sera toujours prioritaire par rapport à celui rentré dans le terminal.


    Lors de la rédaction d'un scénario sans action 'FindDate' il est conseillé de fixer une valeur pour le 'maxJobs'. Sinon le programme sauvegardera l'ensemble des offres d'emploi du site à chaque exécution.

.. code-block:: YAML

   - EXEMPLE:
     - SaveJob: {'maxJobs' = 20}

Action Scroll :
~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **Scroll** permet de simuler l'action de la souris afin de charger les données dynamiques du site. Il nécessite en entrée un type **int** relatif à la distance nécessaire pour afficher les nouvelles informations.

   Paramètre :
      * 'size' : variable principale de l'action. Valeur : taille du scroll nécessaire, type **int**.

.. code-block:: YAML

   - EXEMPLE:
      - Scroll : {'size' : 10, 'possibleAction' : 5}

Action FindDate
~~~~~~~~~~~~~~~~

.. topic:: Présentation :

   L'action **FindDate** permet de repérer la date présente dans la page. En interne, il déterminera si l'offre d'emploi est intéressante ou non (*i.e* si les offres d'emploi ont été publiées après une date pré-déterminée). Il nécessite en entrée le chemin nécessaire à la navigation dans la page HTML.

   Paramètre :

      * 'xpath' : variable principale de l'action. Valeur : chemin xpath de la date ciblée (voir :ref:`Gestiontags`)

.. code-block:: YAML

   - EXEMPLE:
      - FindDate: {'xpath' : '//dd[@class="job_post_date"]//span[@class="field_value"]', 'possibleAction' : 5}

Exemple générique d'un scénario
================================

.. code-block:: YAML

   - EXEMPLE:
      - GoPage: {'url': "https://www.exemple.com/fr/emplois"} # Navigation jusqu'à la page des offres d'emplois
      - FindDate: {'xpath' : '//div[@id="offres"]//span[@class="date_offre"]', 'persitentIndex', 'possibleAction' : 5} # Recherche de la date de la publication de l'offre d'emploi et dépôt d'un marqueur. Si je ne trouve pas de date, je me rends à l'action 5
      - GoNewTab: {'xpath' : '//a[@class="titre_offre"]','persitentIndex'} # Navigation vers la page de l'offre d'emploi et dépôt d'un marqueur
      - SaveJob: {} # Sauvegarde de la page HTML en local de l'offre d'emploi
      - CloseTab: {'nextAction' : 1} # Navigation vers la page précédente
      - ClickPage: {'xpath' : '//div[@button="page_suivante"], 'resetIndex' : [1,2], 'nextAction' : 1} # Navigation vers la page suivante des offres d'emploi après l'action 1

Recommandations
================

   .. warning::

      * Des boucles infinies peuvent être créées lors de la rédaction des 'possibleAction'. Bien veiller à l'enchainement des actions.
      * Il est recommandé de vérifier la synthaxe des scénarios sur le site : 'http://www.yamllint.com/'
      * Lors de la navigation sur certains sites, des boutons initialement actifs et visibles de l'utilisateur humain peuvent devenir cachés pour ce dernier et rester actifs. Par conséquent, le crawl pourra être potentiellement attiré par eux suivant les xpath renseignés. Par conséquent, il est important de déterminer ces boutons pour insérer un xpath prenant en compte la qualité visible ou non du bouton **OU** insérer un xpath permettant de contourner ce bouton.


Exemples de scénarios / fichier '*scenarii.yaml*'
==================================================

.. topic:: scenarii.yaml :

   .. code-block:: YAML

     - SAFRAN:
        - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}
        - FindDate: {'xpath' : "//span[@class='date']", 'persistentIndex', 'possibleAction' : 6}
        - Scroll: {'size': 100, 'persistentIndex'}
        - GoNewTab: {'xpath' : "//a[@class='offer-card']", persistentIndex}
        - SaveJob: {}
        - CloseTab: {'nextAction' : 1}
        - ClickPage: {'xpath' : "//li[@class='next']//a", 'nextAction' : 1, 'resetIndex': [1,3]}

   .. code-block:: YAML

      - BNP:
       - GoPage: {'url': "https://group.bnpparibas/emploi-carriere/toutes-offres-emploi/france"}
       - Scroll: {'size' : 105, 'persistentIndex', 'possibleAction' : 5}
       - GoNewTab: {'xpath' : '//ul[@class="results rh-results"]//li//a', 'persistentIndex', 'possibleAction': 5}
       - SaveJob: {'maxJobs' : 10}
       - CloseTab: {'nextAction' : 1}
       - ClickPage: {'xpath' : '//div[@class="progress-button elastic show-more"]//button', 'nextAction' : 1, 'possibleAction' : 6}
       - ClickPage: {'xpath' : '//li[@class="next"]//a', 'resetIndex' : [1,2], 'nextAction' : 1}


   .. code-block:: YAML

      - SODEXO:
       - GoPage: {'url': "https://sodexo-recrute.talent-soft.com/accueil.aspx?LCID=1036"}
       - FindDate: {'xpath' : '//ul[@class="ts-offer-card-content__list "]/child::li[2]', 'persistentIndex', 'nextAction' : -1}
       - GoNewTab: {'xpath' : '//a[@class="ts-offer-card__title-link  "]', 'persistentIndex'}
       - SaveJob: {}
       - CloseTab: {'nextAction' : 1}

   .. code-block:: YAML

      - TOTAL:
       - GoPage: {'url' : 'https://krb-sjobs.brassring.com/tgnewui/search/home/home?partnerid=30080&siteid=6559#Pays=France&keyWordSearch='}
       - ClickPage: {'xpath' : "//button[@id='searchControls_BUTTON_2']"}
       - FindDate: {'xpath' : "//p[@class='jobProperty position1']", 'persistentIndex', 'possibleAction' : 6}
       - GoNewTab: {'xpath' : "//a[@class='jobProperty jobtitle']", 'persistentIndex'}
       - SaveJob: {}
       - CloseTab: {'nextAction' : 2}
       - ClickPage: {'xpath' : "//a[@id='showMoreJobs']", 'nextAction' : 2, 'resetIndex' : [2,3]}

   .. code-block:: YAML

      - CANAL:
       - GoPage: {'url' : 'https://jobs.canalplus.com/nos-offres/'}
       - Scroll: {'size' : 100, 'persistentIndex'}
       - GoNewTab: {'xpath' : '//div[@class="JobOffersList_JobOffersList_3A33F"]//li[@class="List_boxed__2cbY8 List_borders_default__2dgLN"]//a', 'persistentIndex'}
       - SaveJob: {'maxJobs' : 10}
       - CloseTab: {'nextAction' : 1}

   .. code-block:: YAML

      - DASSAULT:
       - GoPage: {'url' : 'https://careers.3ds.com/fr/jobs?woc=%7B%22pays%22%3A%5B%22pays%2Ffrance%22%5D%7D'}
       - GoNewTab: {'xpath' : '//article[@class="ds-card ds-card--lines ds-card--image "]/child::a', 'persistentIndex', 'possibleAction' : 4}
       - SaveJob: {'maxJobs' : 10}
       - CloseTab: {'nextAction' : 1}
       - ClickPage: {'xpath' : '//li[@class="ds-pagination__next"]//a', 'resetIndex' : [1], 'nextAction' : 1}

   .. code-block:: YAML

      - ACCOR:
       - GoPage: {'url' : 'https://careers.accor.com/Job-vacancy/France,s,4,1.1.html'}
       - FindDate: {'xpath' : '//li[@class="date"]//a/following-sibling::span', 'persistentIndex', 'possibleAction' : 5}
       - GoNewTab: {'xpath' : '//li[@class="labelOffer"]//a[1]', 'persistentIndex'}
       - SaveJob: {}
       - CloseTab: {'nextAction' : 1}
       - ClickPage: {'xpath' : '//ul[@class="nextPage"]//a','resetIndex' : [1,2], 'nextAction' : 1}
