from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox") 

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.google.com")

    if "Google" in driver.title:
        print("Google is alive!")
    else:
        print("Google is down or the page title has changed.")

finally:
    driver.quit()
