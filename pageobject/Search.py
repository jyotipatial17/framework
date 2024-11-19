# search the item
import time
from selenium.webdriver.common.by import By

class search():
    search_buttn='submit_search'

    search_box='search_query'
    time.sleep(4)
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicity_wait(4)

    def search_txt(self,txt):
        self.driver.find_element(By.NAME, self.search_box).send_keys(txt)
    def search_button(self):
        self.driver.find_element(By.NAME, self.search_buttn).click()





