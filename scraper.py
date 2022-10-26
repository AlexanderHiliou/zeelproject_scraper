from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import ast
import os
from dotenv import load_dotenv

load_dotenv()

accounts = os.getenv("ACCOUNTS")

# transform str to a dict
accounts = ast.literal_eval(accounts)


class Scraper:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_and_find_element(self, xpath, value_to_insert=False):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'{xpath}'))
        )
        if value_to_insert:
            self.driver.find_element(
                By.XPATH, f'{xpath}').send_keys(value_to_insert)
        self.driver.find_element(By.XPATH, f'{xpath}').click()


class ZeelProject(Scraper):

    _zeelproject = 'https://zeelproject.com/ru/'

    def __init__(self, link: str, email: str, password: str):
        super().__init__()
        self.link = link
        self.email = email
        self.password = password

    def login(self):
        self.driver.get(self._zeelproject)
        self.wait_and_find_element('//*[@id="login"]/a[1]')
        self.wait_and_find_element('//*[@id="email"]', self.email)
        self.wait_and_find_element('//*[@id="submit_user"]/span[2]')
        self.driver.implicitly_wait(10)
        self.wait_and_find_element('//*[@id="login_password"]')
        self.wait_and_find_element('//*[@id="login_password"]', self.password)
        self.wait_and_find_element('//*[@id="submit_password"]')

    def download(self):
        self.driver.get(self.link)
        download_counter = self.driver.find_element(
            By.CLASS_NAME, 'downloaded')
        if download_counter.text == '0':
            self.driver.find_element(
                By.PARTIAL_LINK_TEXT, 'Скачать 3D модель').click()
            return True
        self.driver.close()
        return False


if __name__ == '__main__':
    for k, v in accounts.items():
        proj = ZeelProject(
            'https://zeelproject.com/ru/32623-coffee-table-heritage.html', k, v)
        proj.login()
        if proj.download():
            break
