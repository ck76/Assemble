from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# http://ds.addsxz.com/2419dshfdrszx.pdf?attname=

import request

browser = webdriver.Chrome()
try:
    browser.get("http://ds.addsxz.com/2419dshfdrszx.pdf?attname=")
    # print(browser.current_url)
    # print(browser.page_source)
finally:
    browser.close()
