from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()
def get_proxy(driver):

    proxy = driver.get('https://free-proxy-list.net/')
    get_raw = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Get raw list"]')))
    get_raw.click()
    popup = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal-body textarea')))
    value_popup = popup.get_attribute('value')
    lst = value_popup.split()
    received_PROXY = (lst[9])
    print(received_PROXY)
    caps = webdriver.DesiredCapabilities.FIREFOX
    caps['marionette'] = True

    caps['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": received_PROXY,
        "ftpProxy": received_PROXY,
        "sslProxy": received_PROXY
    }
get_proxy(driver)