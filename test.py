import pychrome
import time
from parsel import Selector

class Scraper:
    def __init__(self, url):
        self.url = url
        self.browser = pychrome.Browser(url="http://127.0.0.1:9222")
        self.tab = None

    def start_tab(self):
        self.tab = self.browser.new_tab()
        self.tab.start()

    def stop_tab(self):
        if self.tab:
            self.tab.stop()
            self.browser.close_tab(self.tab)

    def scrape(self):
        self.start_tab()
        self.tab.Page.navigate(url=self.url, _timeout=5)
        time.sleep(5)
        html_content = self.tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
        html_content = str(html_content).replace('\u23fd', '')
        selector = Selector(text=html_content)
        paragraph_texts = selector.xpath("//body//p/text()").getall()
        joined_text = ' '.join(paragraph_texts)
        self.stop_tab()
        return joined_text


scraper = Scraper("https://pubs.geoscienceworld.org/aeg/eeg/article-abstract/xxvi/1/135/137377/Computer-Simulation-of-Rockfalls")
print(scraper.scrape())