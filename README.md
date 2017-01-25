PyCon-Sponsors
====================

Scrape sponsors from pycon website and store in a mysql database.

Prerequisites
--------------------
Must have mysql installed.

Installation
--------------------
Create anaconda environment with the included environment.yml file.

```
conda env create -f environment.yml
```

Copy the config.template file and rename config.

Replace username, password, and databse in the new config file.

Running The Crawler
--------------------
From the top level directory, run the following command:

```
scrapy crawl pycon
```
