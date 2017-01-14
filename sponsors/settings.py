"""
Read in settings from configuration file and declare other needed settings.
"""
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('sponsors/config')

BOT_NAME = 'pyconbot'

SPIDER_MODULES = ['sponsors.spiders']

DATABASE = {
    'drivername': 'mysql+pymysql',
    'host': CONFIG['database']['host'],
    'port': CONFIG['database']['port'],
    'username': CONFIG['database']['username'],
    'password': CONFIG['database']['password'],
    'database': CONFIG['database']['database'],
    'query': {"charset": "utf8"}
}

ITEM_PIPELINES = {'sponsors.pipelines.PyConPipeline': 1}

YEAR = 2016
