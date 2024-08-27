import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from random import randint

class ReauestQuotes:
	def __init__(self,tag):
		self.tag = tag
		self.page = "1"
		self.url = f"https://www.goodreads.com/quotes/tag/{self.tag}?page={self.page}"

	def randomQuote(self):
		maxPage = self.getMaxPage()
		if (maxPage != 1):
			self.page = randint(1,maxPage)
		else:
			self.page = 1

		quotes = self.getQuotes()
		maxQuote = len(quotes)
		if (maxQuote != 0):
			randomQuote = randint(1,maxQuote)
			quoteItem = quotes[randomQuote-1].find("div",class_="quoteText")
			text = quoteItem.text.replace("\n","").replace("    ","").strip()
			quote = text[0:text.find("  ―")]

			return quote
		else:
			return None

	def getQuotes(self):
		self.url = f"https://www.goodreads.com/quotes/tag/{self.tag}?page={self.page}"
		soup = self.getSoup()
		quoteItems = soup.find_all("div",class_="quote mediumText")
		return quoteItems

	def getMaxPage(self):
		soup = self.getSoup()
		div =  soup.select_one('#bodycontainer > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(33) > div')
		if div:
			hrefs = div.find_all("a")
			return int(hrefs[-2].text)

		else:
			return 1

	def getSoup(self):
		# headers = {"User-Agent": UserAgent().chrome}
		# print(headers)
		response = requests.get(url=self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
		soup = BS(response.text, "lxml")

		return soup