from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
import time

"""
# Specify the path of the Chrome Driver
chrome_driver_path = "E://SIVARAMAKRISHNAN T//GUVI//Selenium Webdrivers//WebDrivers//chromedriver.exe"

# Setup the Service object
chrome_service = Service(chrome_driver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(chrome_service)
"""

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Maximime the WebBrowser Window
driver.maximize_window()

# Open a website
driver.get("https://www.saucedemo.com/")

# Perform the Actions
User_Name = driver.find_element(By.ID, "user-name")
User_Name.send_keys("standard_user")
User_Name.send_keys(Keys.RETURN)

Password = driver.find_element(By.ID, "password")
Password.send_keys("secret_sauce")
Password.send_keys(Keys.RETURN)

Login = driver.find_element(By.ID, "login-button")
Login.click()

assert "inventory.html" in driver.current_url
"""
It checks if the Current URL of the page contains “inventory.html”.
If the Current URL is correct, the script continues and closes the browser.
If the Current URL is incorrect, an AssertionError is raised, and the script stops
"""

# Suspends the execution for 5 seconds
time.sleep(5)

# Fetch the title of the of the WebPage
Title = driver.title
print("Title:", Title)

# Fetch the Current URL of the of the WebPage
Current_URL = driver.current_url
print("Current URL:", Current_URL)

# Retrieve the entire html source code of the current webpage
page_source = driver.page_source

# Save the html source code to a text file
with open("webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

# Close the WebDriver
driver.quit()
