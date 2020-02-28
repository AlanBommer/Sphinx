.. _ScenariiCAC40:

********************
Scénarios du CAC40
********************

Introduction
=============

   Sur les entreprises et filiales du CAC40, certaines ne sont actuellement pas utilisables par le programme :
      * Legrand, Michelin, Pernod Ricard, Peugeot, Publicis. Ces entreprises publient leurs offres d'emploi sur des sites extérieurs tels que *indeed*, *myworkdayjobs*, *linkedin*,... Pour des raisons juridiques, ces sites ont été écartés.
      * ST Micro Electronics, L'Oreal et Sanofi. Ces entreprises ne classent pas leurs offres par ordre chronologique. Pour éviter des redondances dans l'alimentation de la base de données, ces sites ont été écartés.
      * Vivendi Editis : Cette entreprise est la seule a utiliser un système d'iframe nécessitant une complexification du code et de la rédaction de tous les scénarios. Pour des raisons de practicité, ce format n'étant présent qu'une fois et pour une filiale, ce site a été écarté.
      * L'entreprise Accor était initialement intégré au scénario, néanmoins, lors de la phase de tests, les développeurs du site ont refondu ce dernier en modifiant considérablement la structure. Ils ont, entre autre, supprimé les dates de publication et rangé les offres par ordre alphabétique. Ce site a par conséquent été écarté.

   35 entreprises ou filiales du CAC40 ont été scénarisées afin de permettre au programme de les parcourir. Ces scénarios sont présents ci-dessous.

Scénarios du CAC40
===================

.. literalinclude:: IMG/scenariiCAC40.yaml