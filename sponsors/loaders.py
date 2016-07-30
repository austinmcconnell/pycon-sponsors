from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

class SponsorLoader(ItemLoader):

    default_input_processor = MapCompose(str.strip)
    default_output_processor = Join()
