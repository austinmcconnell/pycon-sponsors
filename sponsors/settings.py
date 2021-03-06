"""Read in settings from configuration file and declare other needed settings."""
# pylint: disable=invalid-name
import configparser

config = configparser.ConfigParser()
config.read('sponsors/config')

BOT_NAME = 'pyconbot'

SPIDER_MODULES = ['sponsors.spiders']

DATABASE = {
    'drivername': 'mysql+pymysql',
    'host': config['database']['host'],
    'port': config['database']['port'],
    'username': config['database']['username'],
    'password': config['database']['password'],
    'database': config['database']['database'],
    'query': {"charset": "utf8"}
}

ITEM_PIPELINES = {
    'sponsors.pipelines.DuplicatesPipeline': 1,
    'sponsors.pipelines.PyConPipeline': 2,
}

YEARS = [2014, 2015, 2016]

LOG_LEVEL = 'INFO'
LOG_FORMAT = '[%(name)s] %(levelname)s: %(message)s'

AUTOTHROTTLE_ENABLED = True
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 43200
DOWNLOAD_DELAY = 2.0
