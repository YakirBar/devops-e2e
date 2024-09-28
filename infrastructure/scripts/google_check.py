from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode (without GUI)
chrome_options.add_argument("--no-sandbox")  # Required for CI/CD environments

# Specify the path to the ChromeDriver (update the path accordingly)
# service = Service("./chromedriver-win64/chromedriver.exe")
service = Service("/usr/bin/chromedriver")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open Google's homepage
    driver.get("https://www.google.com")

    # Check if the title contains "Google"
    if "Google" in driver.title:
        print("Google is alive!")
    else:
        print("Google is down or the page title has changed.")

finally:
    # Close the WebDriver
    driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# # Set Chrome options
# chrome_options = Options()

# # Example: You can add arguments to your Chrome options if needed
# # chrome_options.add_argument("--headless")  # Uncomment for headless mode

# # Connect to the Selenium server running inside the Docker container
# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     options=chrome_options
# )

# try:
#     # Open Google's homepage
#     driver.get("https://www.google.com")

#     # Check if the title contains "Google"
#     if "Google" in driver.title:
#         print("Google is alive!")
#     else:
#         print("Google is down or the page title has changed.")

# finally:
#     # Close the WebDriver
#     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment this line if you want to run headlessly
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=chrome_options)

# try:
#     # Open Google's homepage
#     driver.get("https://www.google.com")

#     # Check if the title contains "Google"
#     if "Google" in driver.title:
#         print("Google is alive!")
#     else:
#         print("Google is down or the page title has changed.")

# finally:
#     # Close the WebDriver
#     driver.quit()
