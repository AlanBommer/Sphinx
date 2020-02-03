********************
Scénarios des sites
********************

Introduction
============

SAFRAN
======

.. code-block:: YAML

   - SAFRAN:
     - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}
     - FindDate: {'tag' : {'class' : 'date'}, 'possibleNode' : 5}
     - ClickPage: {'tag' : {'class' : 'offer-card'}}
     - SaveJob:
     - GoBack: {'nextNode' : 1}
     - ClickPage: {'tag' : {'class' : 'next', 'tag' : {'name' : 'a'}}, 'nextNode' : 1}