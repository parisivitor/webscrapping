from playwright.sync_api import sync_playwright, Error
from bs4 import BeautifulSoup
import sys
import time

class Scrapper():

    def __init__(self):
            self.pw = sync_playwright().start()
            self.max_retries = 3

    def scraping(self, url, retry=0):
        try:
            browser = self.pw.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            soup = BeautifulSoup(page.content(), 'html.parser')
            return page, soup
        except TimeoutError as e:
            if retry < self.max_retries:
                print(f"Erro de TimeoutError. Retentando ({retry + 1}/{self.max_retries})...")
                return self.scraping(url, retry + 1)
            else:
                print(f"\nMáximo de tentativas alcançado. Saindo!")
                time.sleep(2)
                sys.exit()
        except Error as e:
            print(f"\nUm erro occoreu: {e}. Saindo!")
            time.sleep(2)
            sys.exit()

    def close(self):
         self.pw.stop()
