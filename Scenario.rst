********************
Scénarios des sites
********************

Introduction
=============

   Sur les entreprises et filiales du CAC40, certaines ne sont actuellement pas utilisables pour le programme :
      * Legrand, Michelin, Pernod Ricard, Peugeot, Publicis. Ces entreprises publient leurs offres d'emploi sur des sites extérieurs tels que *indeed*, *myworkdayjobs*, *linkedin*,... Pour des raisons juridiques, ces sites ont été écartés.
      * ST Micro Electronics, L'Oreal et Sanofi. Ces entreprises ne classent pas leurs offres par ordre chronologique. Pour éviter des redondances dans l'alimentation de la base de données, ces sites ont été écartés.
      * Vivendi Editis : Cette entreprise est la seule a utiliser un système d'iframe nécessitant une complexification du code et de la rédaction de tous les scénarios. Pour des raisons de practicité, ce format n'étant présent qu'une fois et pour une filiale, ce site a été écarté. 

   37 entreprises ou filiales du CAC40 ont été scénarisées afin de permettre au programme de les parcourir. Ces scénarios sont présents ci-dessous.

Scénarios du CAC40
===================

.. code-block:: YAML

	- ACCOR:
	   - GoPage: {'url' : 'https://careers.accor.com/Job-vacancy/France,s,4,1.1.html'}
	   - FindDate: {'xpath' : '//li[@class="date"]//a/following-sibling::span', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//li[@class="labelOffer"]//a[1]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//ul[@class="nextPage"]//a','resetIndex' : [1,2], 'nextAction' : 1}

	- AIRBUS:
	   - GoPage: {'url': "https://www.airbus.com/careers/search-and-apply/search-for-vacancies.html?filters=filter_2_1072&textsearch=&language=fr"}
	   - GoNewTab: {'xpath' : '//div[@class="wrraper"]//div//div//a', 'persistentIndex', 'possibleAction' : 5}
	   - FindDate: {'xpath' : '//div[@class="row has-padding c-banner__jobinfo"]//div//div/child::span[2]'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//a[@class="c-pagination--item link next c-jobsearchpage_searchlink"]', 'nextAction' : 1, 'resetIndex': 1}

	- AIRLIQUIDE:
	   - GoPage: {'url': "https://www.airliquide.com/fr/carrieres/offres-emploi?searchCriteria[0][key]=LOV18&searchCriteria[0][values][]=9393"}
	   - FindDate: {'xpath' : '//tbody//tr//td[2]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//tbody//tr//td[1]//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//ul[@class="pagination pagination-element pull-right"]//li//a[@title="next page"]', 'resetIndex' : [1,2], 'nextAction' : 1}

	- ARCELOR1:
	   - GoPage: {'url': "https://arcelormittal.jobs.net/fr-FR/search"}
	   - FindDate: {'xpath' : '//td[@class="col-md-2 job-result-date-posted-cell"]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//a[@class="primary-text-color job-result-title"]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@id="jrp-bottom-desktop-pagination"]//div//ul[@class="pagination"]//li//a[@class="next-page-caret"]', 'resetIndex' : [1,2], 'nextAction' : 1}

	- ARCELOR2:
	   - GoPage: {'url' : "https://jobs.arcelormittal.com/Login2.aspx?ci=cs%2fVPE8+4OA%3d&slid=gxp%2faVXf1gE%3d&urltransfer=Login2.aspx"}
	   - ClickPage: {'xpath' : '//input[@id="ctl00_ContentPlaceHolder1_BtnApply"]'}
	   - GoNewTab: {'xpath' : '//tr[contains(@class,"Greycell")]//td//a', 'persistentIndex', 'possibleAction' : 5}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 2}
	   - ClickPage: {'xpath' : '//a[@id="ctl00_ContentPlaceHolder1_NextButton"]', 'resetIndex' : [2], 'nextAction' : 2}

	- ATOS:
	   - GoPage: {'url': "https://jobs.atos.net/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_country=FR"}
	   - GoNewTab: {'xpath' : '//tr[starts-with(@class,"job-tile")]//td//div//div//div//div//h2//a', 'persistentIndex', 'possibleAction' : 4}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//button[@id="tile-more-results"]', 'nextAction' : 1}

	- AXA:
	   - GoPage: {'url' : "https://recrutement.axa.fr/nos-offres-emploi"}
	   - Scroll: {'size' : 100, 'persistentIndex'}
	   - GoNewTab: {'xpath' : '//div[contains(@class,"jobs-list")]//div//a', 'persistentIndex', 'possibleAction' : 5}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[contains(@class,"button-wrapper next")]//button', 'resetIndex' : [1,2], 'nextAction' : 1}

	- BNP:
	   - GoPage: {'url': "https://group.bnpparibas/emploi-carriere/toutes-offres-emploi/france"}
	   - Scroll: {'size' : 105, 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//ul[@class="results rh-results"]//li//a', 'persistentIndex', 'possibleAction': 5}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@class="progress-button elastic show-more"]//button', 'nextAction' : 1, 'possibleAction' : 6}
	   - ClickPage: {'xpath' : '//li[@class="next"]//a', 'resetIndex' : [1,2], 'nextAction' : 1}

	- BOUYGUES:
	   - GoPage: {'url': "https://www.bouygues.com/talents/nos-offres-demploi/"}
	   - FindDate: {'xpath' : '//a[@class="-item"]//div[@class="-infos"]//div[@class="-date"]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//a[@class="-item"]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@class="-link"]//a[@class="load-offers-link js-load-more-offers"]', 'nextAction' : 1}

	- CANAL:
	   - GoPage: {'url' : 'https://jobs.canalplus.com/nos-offres/'}
	   - Scroll: {'size' : 100, 'persistentIndex'}
	   - GoNewTab: {'xpath' : '//div[@class="JobOffersList_JobOffersList_3A33F"]//li[@class="List_boxed__2cbY8 List_borders_default__2dgLN"]//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}

	- CAPGEMINI:
	   - GoPage: {'url': "https://www.capgemini.com/fr-fr/carrieres/offres-emploi/"}
	   - GoNewTab: {'xpath' : '//div[@class="row"]//div//div//div//h3//a', 'persistentIndex', 'possibleAction' : 5}
	   - FindDate: {'xpath' : '//div[@class="row"]/child::div[3]//section/child::p[4]'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//a[@class="section__button pagination__next"]', 'resetIndex' : [1], 'nextAction' : 1}

	- CARREFOUR:
	   - GoPage: {'url': "https://recrute.carrefour.fr/liste-des-offres"}
	   - FindDate: {'xpath' : '//div[@id="offer-list-container"]//div[@class="job-offer-contrat-content"]/child::p[3]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//div[@id="offer-list-container"]//div[@class="job-offer-desc"]//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//li[@class="next square "]//a', 'resetIndex' : [1,2], 'nextAction' : 1}

	- CREDITAGRICOLE1:
	   - GoPage: {'url': "https://www.ca-recrute.fr/offre-de-emploi/liste-offres.aspx"}
	   - FindDate: {'xpath' : '//ul[@class="ts-related-offers__row"]//li/ul/child::li[2]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//a[@class="ts-offer-list-item__title-link "]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//li[@id="ctl00_ctl00_corpsRoot_corps_PaginationLower_liSuivPage"]/a', 'resetIndex' : [1,2], 'nextAction' : 1}

	- CREDITAGRICOLE2:
	   - GoPage: {'url': "https://www.ca-recrute.fr/offre-de-emploi/liste-offres.aspx"}
	   - FindDate: {'xpath' : '//ul[@class="ts-offer-list-item__description "]//li[2]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//a[@class="ts-offer-list-item__title-link "]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//a[@class="ts-ol-pagination-list-item__link ts-ol-pagination-list-item__link--next"]', 'nextAction' : 1, 'resetIndex' : [1,2]}

	- DAILYMOTION:
	   - GoPage: {'url' : "https://jobs.dailymotion.com/"}
	   - GoNewTab: {'xpath' : '//a[@class="job-list-item"]', 'persistentIndex', 'possibleAction' : 4}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@class="text-center col-12"]//button[@class="btn-daily m-4 btn btn-secondary" and contains(text(),"Show more")]', 'nextAction' : 1}

	- DANONE:
	   - GoPage: {'url': "https://jobs.danone.com/search/?q=&locationsearch=France"}
	   - ClickPage: {'xpath' : '//th[@id="hdrDate"]//span//a'}
	   - FindDate: {'xpath' : '//tr[@class="data-row clickable"]/child::td[4]//span[@class="jobDate"]', 'persistentIndex', 'possibleAction' : 6}
	   - GoNewTab: {'xpath' : '//tr[@class="data-row clickable"]//span[@class="jobTitle hidden-phone"]//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 2}
	   - ClickPage: {'xpath' : '//div[@class="pagination-bottom"]//div//div//ul//li[@class="active"]//following-sibling::li//a','resetIndex' : [2,3], 'nextAction' : 2} # nextpage dynamique qui bouge avec le page d'une page à l'autre

	- DASSAULT:
	   - GoPage: {'url' : 'https://careers.3ds.com/fr/jobs?woc=%7B%22pays%22%3A%5B%22pays%2Ffrance%22%5D%7D'}
	   - GoNewTab: {'xpath' : '//article[@class="ds-card ds-card--lines ds-card--image "]/child::a', 'persistentIndex', 'possibleAction' : 4}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//li[@class="ds-pagination__next"]//a', 'resetIndex' : [1], 'nextAction' : 1}

	- DIGITIK:
	   - GoPage: {'url': "https://www.digitick.net/join-us"}
	   - FindDate: {'xpath' : '//div[@class="meta-above-title"]//div[@class="entry-dateline"]//time//a', 'persistentIndex'}
	   - GoNewTab: {'xpath' : '//h1[@class="entry-title p-name"]//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}

	- ESSILOR:
	   - GoPage: {'url': "https://career5.successfactors.eu/career?company=Essilor&career%5fns=job%5flisting%5fsummary&navBarLevel=JOB%5fSEARCH&_s.crb=7V9yhmfeaWq3trQ%2fbKX1RrfhzqA%3d"}
	   - FindDate: {'xpath' : '//div[@class="noteSection"]//div[1]/child::span[2]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//tr[@class="jobResultItem"]//td[1]//div/a[1]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//li[@id="45:_next"]//a', 'resetIndex' : [1,2], 'nextAction' : 1}

	- GAMELOFT:
	   - GoPage: {'url' : "https://www.gameloft.com/corporate/fr/jobs/view-all-opportunities/"}
	   - GoNewTab: {'xpath' : '//ul[@class="jlc-m-listing bp-box list-hover"]/li/a', 'persistentIndex', 'possibleAction' : 4}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@class="moreResults-btn"]//a', 'nextAction' : 1}

	- HERMES:
	   - GoPage: {'url': "https://www.hermesemployeur.com/fr/"}
	   - FindDate: {'xpath' : '//div[@class="row"]//div//a//div/child::span[2]', 'persistentIndex'}
	   - GoNewTab: {'xpath' : '//div[@class="row"]//div//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}

	- KERING:
	   - GoPage: {'url': "https://www.kering.com/fr/talent/offres-d-emploi"}
	   - FindDate: {'xpath' : '//div[@class="news-item__content"]//h6', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//div[@class="news-item__content"]//h2//a[@class="js-collapse"]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//button[@id="load-more-careers"]', 'nextAction' : 1}

	- LVMH:
	   - GoPage: {'url': "https://www.lvmh.fr/talents/nous-rejoindre/nos-offres/liste-des-offres/?job=&place=162&experience=&activity=&contract=&reference=#gt_offers-results"}
	   - GoNewTab: {'xpath' : '//tbody[@id="js-jobs"]//tr//td//div//a', 'persistentIndex', 'possibleAction' : 5}
	   - FindDate: {'xpath' : '//ul[@class="list list--offers"]//li[8]//span'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@class="row align-center leader-mega"]//a[@class="js-load btn btn--std"]', 'nextAction' : 1}

	- ORANGE:
	   - GoPage: {'url' : "https://orange.jobs/jobs/search.do?lang=FR"}
	   - Scroll: {'size' : 106, 'persistentIndex'}
	   - GoNewTab: {'xpath' : '//div[@class="dgt-list oj-jobslist"]//li//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}

	- SAFRAN:
	  - GoPage: {'url': "https://www.safran-group.com/fr/emplois?pays=France"}
	  - FindDate: {'xpath' : "//span[@class='date']", 'persistentIndex', 'possibleAction' : 6}
	  - Scroll: {'size': 100, 'persistentIndex'}
	  - GoNewTab: {'xpath' : "//a[@class='offer-card']", persistentIndex}
	  - SaveJob: {}
	  - CloseTab: {'nextAction' : 1}
	  - ClickPage: {'xpath' : "//li[@class='next']//a", 'nextAction' : 1, 'resetIndex': [1,3]}

	- SAINTGOBAIN:
	   - GoPage: {'url': "https://joinus.saint-gobain.com/fr?country=FR&search=&page=0"}
	   - FindDate: {'xpath' : '//div[@class="views-row"]//div/a/child::div[5]//div', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//div[@class="views-row"]//div/a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//li[@class="pager__item pager__item--next"]/a', 'resetIndex' : [1,2], 'nextAction' : 1}

	- SCHNEIDER:
	   - GoPage: {'url': "https://schneiderele.taleo.net/careersection/2/jobsearch.ftl?lang=fr-FR&keyword=&CATEGORY=-1&LOCATION=-1"}
	   - GoNewTab: {'xpath' : '//ul[@id="jobList"]//li/child::div[2]//div/span/a', 'persistentIndex', 'possibleAction' : 5}
	   - FindDate: {'xpath' : '//div[@class="editablesection"]//div[@id="requisitionDescriptionInterface.ID1688.row1"]/child::span[2]'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//span[@class="pagerlink"]/a', 'resetIndex' : [1], 'nextAction' : 1}

	- SOCIETEGENERALE:
	   - GoPage: {'url' : "https://careers.societegenerale.com/rechercher?query="}
	   - Scroll: {'size' : 88, 'persistentIndex'}
	   - GoNewTab: {'xpath' : '//div[@class="hit-text"]/a', 'persistentIndex', 'possibleAction' : 1}
	   - FindDate: {'xpath' : '//div[@class="container"]//div//div//div/child::div[4]/child::span[2]//strong', 'possibleAction' : 1}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}

	- SODEXO:
	   - GoPage: {'url': "https://sodexo-recrute.talent-soft.com/accueil.aspx?LCID=1036"}
	   - FindDate: {'xpath' : '//ul[@class="ts-offer-card-content__list "]/child::li[2]', 'persistentIndex', 'nextAction' : -1}
	   - GoNewTab: {'xpath' : '//a[@class="ts-offer-card__title-link  "]', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}

	- THALES:
	   - GoPage: {'url': "https://jobs.thalesgroup.com/search-jobs?_ga=2.259037065.2075221412.1572629140-455965246.1572429512"}
	   - FindDate: {'xpath' : '//span[@class="job-date-posted"]', 'persistentIndex', 'possibleAction' : 5}
	   - GoNewTab: {'xpath' : '//section[@id="search-results-list"]//ul//li//a', 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//div[@class="pagination-paging"]//a[@class="next"]','resetIndex' : [1,2], 'nextAction' : 1}

	- TOTAL:
	   - GoPage: {'url' : 'https://krb-sjobs.brassring.com/tgnewui/search/home/home?partnerid=30080&siteid=6559#Pays=France&keyWordSearch='}
	   - ClickPage: {'xpath' : "//button[@id='searchControls_BUTTON_2']"}
	   - FindDate: {'xpath' : "//p[@class='jobProperty position1']", 'persistentIndex', 'possibleAction' : 6}
	   - GoNewTab: {'xpath' : "//a[@class='jobProperty jobtitle']", 'persistentIndex'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 2}
	   - ClickPage: {'xpath' : "//a[@id='showMoreJobs']", 'nextAction' : 2, 'resetIndex' : [2,3]}

	- VEOLIA:
	   - GoPage: {'url': "https://veolia.taleo.net/careersection/extexp/jobsearch.ftl?lang=fr_FR&back_param=2"}
	   - GoNewTab: {'xpath' : '//ul[@id="jobList"]//li/child::div[2]//div/span/a', 'persistentIndex', 'possibleAction' : 5}
	   - FindDate: {'xpath' : '//div[@class="editablesection"]//div[@id="requisitionDescriptionInterface.ID1758.row1"]/child::span[2]'}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//span[@class="pagerlink"]/a', 'resetIndex' : [1], 'nextAction' : 1}

	- VINCI:
	   - GoPage: {'url' : "https://emplois.vinci.com/recherche-d'offres"}
	   - GoNewTab: {'xpath' : '//ul[@class="list"]/li/a', 'persistentIndex', 'possibleAction' : 4}
	   - SaveJob: {}
	   - CloseTab: {'nextAction' : 1}
	   - ClickPage: {'xpath' : '//a[@class="next"]', 'resetIndex' : [1], 'nextAction' : 1}
