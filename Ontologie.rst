************************
Rédaction des scénarios
************************

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

Liste des actions
++++++++++++++++++

   Les actions sont au nombre de 6 et elles permettent d'avoir un impact déterminé sur la page web.

   #. GoPage, pour se rendre sur une page donnée
   #. ClickPage, pour clicker sur un lien donné
   #. SaveJob, pour sauvegarder l'emploi
   #. Scroll, pour faire dérouler la page actuelle
   #. GoBack, pour revenir en arrière
   #. FindDate, pour chercher la date des offres d'emploi dans la page actuelle

Gestion des nodes
++++++++++++++++++

   Un node est un point de repère permettant au programme de naviguer au sein d'un scénario. Chaque node représente une action. C'est l'élément utilisé dans le code pour traiter les scénarios.

   1. La première action du scénario renvoie au premier node du scénario, indexé '0'
   2. Un scénario comprend plusieurs actions. Il existe 3 possibilités permettant d'exprimer quelle est la prochaine action à exécuter.
   3. Par défaut, la prochaine action exécutée est la ligne suivante du scénario.
   4. Nous pouvons également, en paramètre de l'action, définir le prochain node à exécuter : 

      * *nextNode* = node qui sera traité à la fin de l'action si elle s'éxécute correctement, par défaut 'nextNode' renvoie au node de l'action suivante'
      * *possibleNode* = node qui sera appelé si l'action actuelle ne remplit pas son objectif *(ex : si l'action FindDate ne trouve pas de date ou si l'action "ClickPage" ne trouve pas de bouton 'Page suivante' )*

   5. Cas particulier. En cas d'erreur lors de l'exécution, s'il n'y a aucun 'possibleNode', alors le scénario s'arrête.

.. _Gestiontags:

Gestion des tags
+++++++++++++++++

  1. Le programme s'appuie sur les élements du dom HTML pour scrapper les données. Nous les appellerons des tags.
  2. Les tags sont définis par un couple (clé, valeur).
  3. Les (clés,valeurs) possibles pour un tag sont les suivantes :

      * Pour une balise : clé = 'balise' & valeur = 'a', 'img', 'span', 'div', 'li',...

          .. code-block:: YAML

            - Exemple: {'balise' : 'a'}

      * Pour un attribut : clé = 'href', 'class', 'id',... & valeur = 'string'

          .. code-block:: YAML

            - Exemple: {'class' : 'labelOffer'}

      * Pour un texte brut : clé = 'texte' & valeur = 'string'

          .. code-block:: YAML

            - Exemple: {'texte' : '02/05/2020'}

  4. Chaque fois que nous écrivons un couple (clé,valeur) nous devons le spécifier dans un dictionnaire dont la clé est 'tag'.

    .. code-block:: YAML

       - Exemple: {'tag' : {'class' : 'labelOffer'}}

  5. Afin d'arriver à la donnée spécifiée, il sera parfois nécessaire de parcourir différents tags inclus les uns dans les autres. Pour cela, il est possible d'effectuer une imbrication de tags.

     .. code-block:: YAML

       - Exemple: {'tag' : {'class' : 'labelOffer', 'tag' : {'balise' : 'a'}}

  Ici, le programme va rechercher un tag correspondant à un attribut 'class' dont la valeur est 'labelOffer'. Une fois déterminé, il va rechercher à l'intérieur de ce bloc html le premier tag correspondant à la balise 'a'. Pour explication, lors d'une recherche d'un tag, le programme récupèra une liste de tous les résultats correspondants à ce tag.

  6. Attention, si rien n'est spécifié, seul le premier résultat de la recherche sera pris en compte.

    .. code-block:: YAML

      - Exemple: {'tag' : {'class' : 'labelOffer', 'tag' : {'balise' : 'a'}}

    .. code-block:: HTML

      <div>
        <span class = 'labelOffer' href = 'url'>
          <a> Publié le </a> <!-- Résultat de la recherche ci-dessus -->
          <a> 05/02/2020 </a>
        </span>
      </div>

  7. Suite à la recherche d'un tag, il sera parfois nécessaire d'accéder à un élément spécifique de la liste des résultats. Pour cela, il est possible de définir le paramètre 'mark : n' avec le numéro de l'indice recherché.

    .. code-block:: YAML

       - Exemple: {'tag' : {'class' : 'labelOffer', 'tag' : {'balise' : 'a', 'mark' : 1}}

  Ici, nous prendrons l'indice numéro 1 de la liste des résultats. Dans l'exemple ci-dessus, le résultat sera donc '05/02/2020' et non 'Publié le'.

  8. La recherche des tags ne peut s'effectuer qu'au travers des actions "FindDate" et "ClickPage". Pour "FindDate", le programme cherchera une valeur textuelle au format d'une date. Pour "ClickPage", le programme cherchera une url.

  .. warning::

     1. Via cette gestion des tags, il est possible d'arriver rapidement à la donnée voulue. Pour cela, il est conseillé de déterminer la valeur d'un tag unique. Indice : quand le code HTML est bien écrit, la valeur d'un attribut 'id' est unique.
     2. Il est préférable de prendre des tags dans la page HTML qui ne sont pas susceptibles d'être modifiés.


Gestion des index
+++++++++++++++++

  1. Afin de naviguer entre les différentes offres d'emploi, le programme a besoin de poser des points de repères pour ensuite jalonner son trajet.

  2. Ces points sont nommés 'persistentIndex'. Ils doivent être définis dans le paramétrage des actions "ClickPage" ou "FindDate" si les noeuds liés en ont besoin.

   .. code-block:: YAML

      - EXEMPLE:
        - GoPage: {'url': "https://www.exemplesiteemplois.com/fr"} 
        - ClickPage: {'tag' : {'class': 'primaryButton'}} # Noeud permettant d'accéder aux offres d'emploi
        - FindDate: {'tag' : {'class' : 'date'}, 'persistentIndex', 'possibleNode' : 5} # Je marque l'emplacement de ma première balise liée à la date.
        - ClickPage: {'tag' : {'class' : 'offer-card'}, 'persistentIndex'} # Je marque l'emplacement de ma première balise liée à mon emploi.
        - SaveJob:
        - ...

  3. Ainsi, le programme peut naviguer de noeud en noeud en connaissant les balises déjà visitées.

  4. La réinitialisation de l'index persistant se fait dans le paramétrage d'une action. On utilise la clé 'resetIndex' et une valeur 'liste[int]' relative au numéro du node dans lequel le marqueur a été initialisé.

   .. code-block:: YAML

      - EXEMPLE:
        - GoPage: {'url': "https://www.exemplesiteemplois.com/fr"} 
        - ClickPage: {'tag' : {'class': 'primaryButton'}} # Action permettant d'accéder aux offres d'emploi
        - FindDate: {'tag' : {'class' : 'date'}, 'persistentIndex', 'possibleNode' : 5} # Je marque l'emplacement de ma première balise liée à la date.
        - ClickPage: {'tag' : {'class' : 'offer-card'}, 'persistentIndex'} # Je marque l'emplacement de ma première balise lié à mon emploi.
        - SaveJob:
        - GoBack: {'nextNode' : 1} # Je reviens au node 1 et repère la balise déjà visitée grâce au marqueur déposé
        - ClickPage: {'tag' : {'class' : 'next', 'tag' : {'balise' : 'page'}}, 'resetIndex' : [1,2], 'nextNode' : 1} # Remise à zéro du marqueur défini dans le noeud 2 : "FindDate" lorsque le scénario se rendra sur la page suivante du site.

Description des actions :
=========================

Action GoPage :
++++++++++++++++

.. topic:: Présentation :

   L'action **GoPage** permet d'accéder à la page web des offres. Il nécessite en entrée un lien internet qui renvoie à la page des offres d'emplois de l'entreprise visée.

   Paramètre :

      * 'url' : variable principale de l'action. Valeur : adresse url renvoyant à la page web des offres d'emplois.

.. code-block:: YAML

   - EXEMPLE:
      - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}

Action ClickPage
+++++++++++++++++

.. topic:: Présentation :

   L'action **ClickPage** permet de cliquer sur un lien url spécifique : fonction recherche, accéder à l'offre d'emploi, accéder à la page suivante du site. Il nécessite en entrée le chemin nécessaire à la navigation dans la page HTML.

   Paramètre :

      * 'tag' : variable principale de l'action. Valeur : encapsulage des tags (voir :ref:`Gestiontags`)

.. code-block:: YAML

   - EXEMPLE:
      - ClickPage: {'tag' : {'class' : labelOffer', 'tag' : {'balise' : 'a'}, 'persistentIndex'}

Action SaveJob
+++++++++++++++

.. topic:: Présentation :

   L'action **SaveJob** permet de sauvegarder la page HTML de l'offre d'emploi. Il ne nécessite pas de paramètre. Le programme est chargé d'effectuer la sauvegarde locale puis le transfert sur la base de donnée.

.. code-block:: YAML

   - EXEMPLE:
     - SaveJob:

Action Scroll
++++++++++++++

.. topic:: Présentation :

   L'action **Scroll** permet de simuler l'action de la souris afin de charger les données dynamiques du site. Il nécessite en entrée un entier int relatif à la distance nécessaire pour afficher les nouvelles informations.

   Paramètre :
      * 'size' : variable principale de l'action. Valeur : taille du scroll nécessaire.

.. code-block:: YAML

   - EXEMPLE:
      - Scroll : {'size' : 10, 'possibleNode' : 5}

Action GoBack
++++++++++++++

.. topic:: Présentation :

   L'action **GoBack** permet d'effectuer un retour en arrière pour retourner sur la page url précédente. Il nécessite en entrée le renvoi sur l'action à exécuter à l'issue

   Paramètre :

      * 'nextNode' : valeur principale de l'action. Valeur : node de l'action à exécuter à l'issue.

.. code-block:: YAML

   - EXEMPLE:
      - GoBack: {'nextNode' : 2}

Action FindDate
++++++++++++++++

.. topic:: Présentation :

   L'action **FindDate** permet de repérer la date présente dans la page. En interne, il déterminera si l'offre d'emploi est intéressante ou non (*i.e* si les offres d'emploi ont été publiées après une date pré-déterminée). Il nécessite en entrée le chemin nécessaire à la navigation dans la page HTML.

   Paramètre :

      * 'tag' : variable principale de l'action. Valeur : encapsulage des tags (**cf "Gestion des tags"**)

.. code-block:: YAML

   - EXEMPLE:
      - FindDate: {'tag' : {'class' : 'date', 'tag' : {'balise' : 'span'}}, 'possibleNode' : 5}

Exemple d'un scénario générique : 
=================================

.. code-block:: YAML 

   - EXEMPLE:
      - GoPage: {'url': "https://www.exemple.com/fr/emplois"} # Navigation jusqu'à la page des offres d'emplois
      - FindDate: {'tag' : {'class' : 'date'}, 'persitentIndex', 'possibleNode' : 5} # Recherche de la date de la publication de l'offre d'emploi et dépôt d'un marqueur. Si je ne trouve pas de date, je me rends au noeud 5
      - ClickPage: {'tag' : {'class' : 'job-offer'},'persitentIndex'} # Navigation vers la page de l'offre d'emploi et dépôt d'un marqueur
      - SaveJob: # Sauvegarde de la page HTML en local de l'offre d'emploi
      - GoBack: {'nextNode' : 1} # Navigation vers la page précédente
      - ClickPage: {'tag' : {'class' : 'next', 'tag' : {'balise' : 'page'}}, 'resetIndex' : [1,2], 'nextNode' : 1} # Navigation vers la page suivante des offres d'emploi après le noeud 1

Recommandations :
=================

   .. warning::

      * Des boucles infinies peuvent être créées lors de la rédaction des 'possibleNode'. Bien veiller à l'enchainement des actions.
      * Il est recommandé de vérifier la synthaxe des scénarios sur le site : 'http://www.yamllint.com/'


Exemples de scénarios / fichier '*scenarii.yaml*'
==================================================

.. topic:: SAFRAN

   .. code-block:: YAML

      - SAFRAN:
        - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}
        - FindDate: {'tag' : {'class' : 'date'} 'possibleNode' : 5}
        - ClickPage: {'tag' : {'class' : 'offer-card'}}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : {'class' : 'next', 'tag' : {'balise' : 'a'}}, 'nextNode' : 1}

.. topic:: BNP

  .. code-block:: YAML

   - BNP:
       - GoPage: {'url': "https://group.bnpparibas/emploi-carriere/toutes-offres-emploi/france"}
       - Scroll: {'size' : 10, 'possibleNode' : 5}
       - ClickPage: {'tag' : {'class' : }}
       - SaveJob:
       - GoBack: {'nextNode' : 1}
       - ClickPage: {'tag' : 'progress-buton elastic show-more', 'nextNode' : 1, 'possibleNode' : 6}
       - ClickPage: {'tag' : 'next', 'nextNode' : 1}

.. topic:: SODEXO

  .. code-block:: YAML

     - SODEXO:
       - GoPage: {'url': "https://fr.sodexo.com/home/nous-rejoindre/rejoignez-nos-equipes.html"}
       - FindDate: {'tag' : ts-offer-card-content offerContent', 'index' : 1 }
       - ClickPage: {'tag' : 'ts-offer-card__title'}
       - SaveJob:
       - GoBack: {'nextNode' : 1}
       - ClickPage: {'tag' : 'ts-ol-pagination-list-item__link ts-ol-pagination-list-item__link--next', 'nextNode' : 1}

.. topic:: TOTAL

  .. code-block:: YAML

      - TOTAL:
        - GoPage: {'url' : 'https://krb-sjobs.brassring.com/tgnewui/search/home/home?partnerid=30080&siteid=6559#Pays=France&keyWordSearch='}
        - ClickPage: {'tag' : 'primaryButton ladda-button ng-binding'}
        - FindDate: {'tag' : 'jobProperty position1'}
        - ClickPage: {'tag' : 'jobProperty jobtitle'}
        - SaveJob:        
        - GoBack: {'nextNode' : 2}
        - ClickPage: {'tag' : showMoreJobs UnderLineLink ng-binding', 'nextNode' : 2}

.. topic:: CANAL

  .. code-block:: YAML

      - CANAL:
        - GoPage: {'url' : 'https://www.vousmeritezcanalplus.com/metiers.html'}
        - FindDate: {'tag' : 'srJobListPublishedSince'}
        - ClickPage: {'tag' : 'srJobListJobOdd'}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
 
.. topic:: DASSAULT

  .. code-block:: YAML

      - DASSAULT:
        - GoPage: {'url' : 'https://careers.3ds.com/fr/jobs?woc=%7B%22pays%22%3A%5B%22pays%2Ffrance%22%5D%7D'}
        - ClickPage: {'tag' : 'ds-card ds-card--lines ds-card--image ', 'possibleNode' : 4}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - ClickPage: {'tag' : 'ds-pagination__next', 'nextNode' : 1}

.. topic:: ACCOR

  .. code-block:: YAML

      - ACCOR:
        - GoPage: {'url' : 'https://careers.accor.com/Job-vacancy/France,s,4,1.1.html'}
        - FindDate: {'tag' : {'class' : 'date', 'tag' : {'balise' : 'span'}}, 'possibleNode' : 5}
        - ClickPage: {'tag' : {'class' : labelOffer', 'tag' : {'balise' : 'a'}}
        - SaveJob:
        - GoBack: {'nextNode' : 1}
        - CLikPage: {'tag' : {'class' : 'nextPage', {'class' : 'on'}}, 'nextNode' : 1}

