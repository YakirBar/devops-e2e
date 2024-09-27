from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup WebDriver (for Chrome)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Path to your WebDriver
webdriver_service = Service('path/to/chromedriver')

# Initialize WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # Open Google's website
    driver.get("https://www.google.com")
    
    # Wait for the page to load
    time.sleep(2)  # Adjust sleep time if needed

    # Check if the title contains "Google"
    if "Google" in driver.title:
        print("Google is alive!")
    else:
        print("Google is not accessible!")

finally:
    # Close the browser
    driver.quit()
