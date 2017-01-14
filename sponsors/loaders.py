"""
This module defines loaders to populate scraped items. They can automate
common tasks and simplify the data loading process.
"""
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join


class SponsorLoader(ItemLoader):
    """
    Accepts ItemLoader and processes input with MapCompose and Join
    """
    default_input_processor = MapCompose(str.strip)
    default_output_processor = Join()
