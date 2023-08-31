from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from utils.selenium_driver import SeleniumDriver as SD

class CSEScrape:
    @staticmethod
    def initDriver():
        sd = SD('https://enroll.wisc.edu')
        
        el_login_selector= sd.initElementByClass('btn-primary')

        sd.waitElementInvisibile(el_login_selector, 5)

        el_search_selector = sd.initElementByClass('mat-raised-button')

        el_search_action = sd.waitElementVisibile(el_search_selector, 60)
        
        el_search_action.click()

        el_course_listings = sd.initElementByClass("ng-star-inserted")

        el_course_action = sd.waitElementVisibile(el_course_listings, 1)

        el_course_action.click()

        sd.waitElementVisibile(el_login_selector, 120)


        # driver = sd.getDriver()
        # driver.execute_script("arguments[0].click();", el_search_submit)
        print("done")   




if __name__ == '__main__':
    CSEScrape.initDriver()