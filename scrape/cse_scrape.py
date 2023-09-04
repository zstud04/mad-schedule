from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from utils.selenium_driver import SeleniumDriver as SD

from utils.cse.cse_helper import CSEHelper

from utils.scrape_helper import ScrapeHelper as utils

class CSEScrape:
    

    sd = SD(CSEHelper.BASE_URL)
    # el_login_selector= sd.initElementByClass(CSEHelper.login_selector_1)
    el_search_selector = utils.defer(sd.findElement, CSEHelper.search_selector_1, By.CLASS_NAME, 5)
    
    el_login_selector = utils.defer(sd.initElementByClass, CSEHelper.login_selector_1)

    el_course_listings = utils.defer(sd.findElement, CSEHelper.course_listings, By.XPATH, 5)

    @staticmethod
    def initDriver():
        #sd = SD(CSEHelper.BASE_URL)
        
        el_login_selector = CSEScrape.el_login_selector()
        CSEScrape.sd.waitElementInvisible(el_login_selector, 30)       

        CSEScrape.el_search_selector().click()

        CSEScrape.el_course_listings().click()

        CSEScrape.sd.waitElementVisibile(el_login_selector, 120)

        print("done")   





if __name__ == '__main__':
    CSEScrape.initDriver()