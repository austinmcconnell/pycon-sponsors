"""This file defines classes using Scrapy Items and Fields which will hold scraped data."""
from scrapy.item import Item, Field


class Sponsor(Item):
    """Sponsor container for scraped data."""

    year = Field()
    name = Field()
    url = Field()
    sponsor_level = Field()
    description = Field()

    def __str__(self):
        """Overwriting str method to stop massive output vomit when scrapy is run."""
        return ''
