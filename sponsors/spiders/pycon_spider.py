"""Spider to scrape sponsors from us.pycon.org."""
from scrapy.spiders import Spider
from scrapy.selector import Selector
from sponsors.items import Sponsor
from sponsors.loaders import SponsorLoader
from sponsors.settings import YEARS
import re


class PyConSpider(Spider):
    """Spider for pycon.org/sponsors."""

    name = 'pycon'
    allowed_domains = ['us.pycon.org']
    start_urls = []
    for year in YEARS:
        start_urls.append('https://us.pycon.org/{}/sponsors'.format(year))

    search_list_xpath = '//*[@class="sponsor-content"]'
    search_fields = {
        'name': './h4/text()',
        'url': './p[1]/a/text()',
        'sponsor_level': '../../../../h2/text()',
        'description': './p[3]/text()'
    }

    def parse(self, response):
        """Default callback used by Scrapy to process downloaded reponses."""
        selector = Selector(response)

        # Iterate over properties
        for sponsor in selector.xpath(self.search_list_xpath):

            loader = SponsorLoader(Sponsor(), selector=sponsor)

            # Iterate over fields and add xpath to the loader
            for field, xpath in iter(self.search_fields.items()):
                loader.add_xpath(field, xpath)

            m = re.search('\d\d\d\d', response.request.url)
            item = loader.load_item()
            item['year'] = m.group(0)

            yield item
