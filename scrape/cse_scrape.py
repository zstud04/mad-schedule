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

    el_course_listings = utils.defer(sd.initElements, CSEHelper.course_listings, By.XPATH, 5)

    el_catalog_ref = utils.defer(sd.findElement, CSEHelper.catalog_ref, By.CLASS_NAME, 5)

    el_course_title = utils.defer(sd.findElement, CSEHelper.course_title, By.CLASS_NAME, 5)

    el_course_description = utils.defer(sd.findElement, CSEHelper.course_description, By.XPATH, 5)

    el_course_details = utils.defer(sd.findElement, CSEHelper.course_details, By.XPATH)

    el_subj_notes = utils.defer(sd.findElement, CSEHelper.subj_notes, By.XPATH)

    el_course_section_button = utils.defer(sd.findElement, CSEHelper.course_section_btn, By.XPATH, 5)

    el_section_dropdown_btn = utils.defer(sd.findElement, CSEHelper.section_dropdown_btn, By.XPATH, 10)

    el_section_availability = utils.defer(sd.findElement, CSEHelper.section_availability, By.XPATH, 5)

    el_section_back_btn = utils.defer(sd.findElement, CSEHelper.section_back_btn, By.XPATH, 10)

    el_next_result_query_btn = utils.defer(sd.findElement, CSEHelper.next_result_query_btn, By.XPATH, 5)


    @staticmethod
    def executeMain():
        #sd = SD(CSEHelper.BASE_URL)
        
        
        el_login_selector = CSEScrape.el_login_selector()
        CSEScrape.sd.waitElementInvisible(el_login_selector, 30)       

        CSEScrape.el_search_selector().click()

        CSEScrape.el_course_listings()[0].click()

        CSEScrape.course_entry_iter()
        
        ##TODO: delete when testing is done

        CSEScrape.sd.waitElementVisibile(el_login_selector, 200)
        

        print("done")   

    @staticmethod
    def course_entry_iter():
        listings = CSEScrape.el_course_listings()
  
        for listing in listings:
            listing.click()
            CSEScrape.course_scrape()

        print("DONE!")
        CSEScrape.el_next_result_query_btn().click()
            

    
    @staticmethod
    def course_scrape():
        print(CSEScrape.el_catalog_ref().text)
        print(CSEScrape.el_course_title().text)

        print(CSEScrape.el_course_description().text)

        print(CSEScrape.el_course_details().text)

        print(CSEScrape.el_subj_notes().text)
        
        CSEScrape.el_course_section_button().click()

        CSEScrape.el_section_dropdown_btn().click()

        print("----")

        print(CSEScrape.el_section_availability().text)
        
        CSEScrape.el_section_back_btn().click()




if __name__ == '__main__':
    CSEScrape.executeMain()