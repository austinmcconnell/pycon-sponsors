from scrapy.item import Item, Field

class Sponsor(Item):
    """
    Sponsor container for scraped data
    """
    year = Field()
    name = Field()
    url = Field()
    sponsor_level = Field()
    description = Field()
