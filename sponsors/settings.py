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

ITEM_PIPELINES = {'sponsors.pipelines.PyConPipeline':1}

YEAR = 2016