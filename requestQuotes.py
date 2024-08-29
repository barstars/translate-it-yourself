import aiohttp
import asyncio
from bs4 import BeautifulSoup as BS
from random import randint

class RequestQuotes:
    def __init__(self, tag):
        self.tag = tag
        self.page = "1"
        self.url = f"https://www.goodreads.com/quotes/tag/{self.tag}?page={self.page}"

    async def random_quote(self):
        max_page = await self.get_max_page()
        if max_page != 1:
            self.page = randint(1, max_page)
        else:
            self.page = 1

        quotes = await self.get_quotes()
        max_quote = len(quotes)
        if max_quote != 0:
            random_quote = randint(1, max_quote)
            quote_item = quotes[random_quote - 1].find("div", class_="quoteText")
            text = quote_item.text.replace("\n", "").replace("    ", "").strip()
            quote = text[0:text.find("  ―")]

            return quote
        else:
            return None

    async def get_quotes(self):
        self.url = f"https://www.goodreads.com/quotes/tag/{self.tag}?page={self.page}"
        soup = await self.get_soup()
        quote_items = soup.find_all("div", class_="quote mediumText")
        return quote_items

    async def get_max_page(self):
        soup = await self.get_soup()
        div = soup.select_one(
            '#bodycontainer > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(33) > div'
        )
        if div:
            hrefs = div.find_all("a")
            return int(hrefs[-2].text)
        else:
            return 1

    async def get_soup(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                text = await response.text()
                soup = BS(text, "lxml")
                return soup