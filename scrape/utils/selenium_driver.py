import string
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

class SeleniumDriver:

    def __init__(self, base_url):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        val = base_url
        self.driver.get(val)

    def initElementById(self, id:string):
        return (By.ID, id)

    def initElementByXPath(self, path:string):
        return (By.XPATH, path)

    def initSelectById(self, id:string):
        return Select(self.driver.find_element(By.ID, id))
    
    def initElementByClass(self, class_name:string):
        return (By.CLASS_NAME, class_name)
    
    def waitElementVisibile(self, element, time:int):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(element)
        )
    def waitElementInvisible(self, element, time:int):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(element)
        )
    def initElementsByClass(self, class_name:string):
        return self.driver.find_elements(By.XPATH, class_name)

    def initElementByTag(self, tag_name:string):
        return self.driver.find_element(By.TAG_NAME, tag_name)

    def findElement(self, select_string:string, select_type, select_time:int=1):
        return WebDriverWait(self.driver, select_time).until(
            EC.visibility_of_element_located((select_type, select_string))
        )
    
    def switchToIFrame(self):
        self.driver.switch_to.default_content()
    
    
    
    def clickElement(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        
    def getDriver(self):
        return self.driver
