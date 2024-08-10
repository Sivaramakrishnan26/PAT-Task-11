from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.wait import WebDriverWait
from selenium.webdriver.support import ExpectedConditions as EC
import time


class Drag_and_Drop:  # Create a Class
    def __init__(self):  # Constructor method
        self.driver = webdriver.Chrome()  # Create a Chrome WebDriver Instance
        self.driver.maximize_window()  # Maximize the Window
        self.driver.implicitly_wait(10)
        self.driver.get("https://jqueryui.com/droppable/")  # Open a website


    def perform_drag_and_drop(self):  # Method to perform Drag and Drop
        wait = WebDriverWait(self.driver, 10)
        drag_element = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        drop_element = wait.until(EC.presence_of_element_located((By.ID, "droppable")))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_element, drop_element).perform()


    def quit(self):  # Method to close the WebDriver
        self.driver.quit()


# Main Execution
if __name__ == "__main__":
    try:
        DragDrop = Drag_and_Drop()
        DragDrop.perform_drag_and_drop()
    finally:
        DragDrop.quit()
        
