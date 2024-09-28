# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # Configure Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Runs Chrome in headless mode (without GUI)

# # Specify the path to the ChromeDriver (update the path accordingly)
# service = Service("C:\\Users\\yakir\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)

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


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chrome_options = Options()

# Example: You can add arguments to your Chrome options if needed
# chrome_options.add_argument("--headless")  # Uncomment for headless mode

# Connect to the Selenium server running inside the Docker container
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=chrome_options
)

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
