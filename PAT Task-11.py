from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Drag_and_Drop:  # Create a Class
    def __init__(self):  # Constructor method
        self.driver = webdriver.Chrome()  # Create a Chrome WebDriver Instance
        self.driver.maximize_window()  # Maximise the Window
        self.driver.implicitly_wait(10)
        self.driver.get("https://jqueryui.com/droppable/")  # Open a website


    def perform_drag_and_drop(self):  # Method to perform Drag and Drop
        wait = WebDriverWait(self.driver, 10)

        iframe = self.driver.find_element(By.XPATH, "//iframe[@src='/resources/demos/droppable/default.html']")
        self.driver.switch_to.frame(iframe)  # Switch to iframe

        drag_element = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        drop_element = wait.until(EC.presence_of_element_located((By.ID, "droppable")))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_element, drop_element).perform()  # Perform Drag and Drop


    def quit(self):  # Method to close the WebDriver
        self.driver.quit()


# Main Execution
if __name__ == "__main__":
    DragDrop = Drag_and_Drop()

    try:
        DragDrop.perform_drag_and_drop()
    
    except Exception as e:
        print(f"Error Occured: {e}")
    
    finally:
        DragDrop.quit()
