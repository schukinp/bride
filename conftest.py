import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from data import base_url
from selene.api import config, browser


options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
#options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
config.timeout = 10
browser.set_driver(driver)


@pytest.fixture(scope='session')
def open_base_url():
    browser.open_url(base_url)
    yield
    driver.quit()
