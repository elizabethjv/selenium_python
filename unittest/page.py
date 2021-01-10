#Each page within a website are are going to be defined inside a class, for easy accessbility

from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

#Base class for all the pages, need to pass the webdriver in the constructor. The child classes created will then inherit the webdriver
class BasePage(object):  #Inherit object
    def __init__ (self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()
    # search_text_element = "hello"       #this invokes  __set__(self,MainPage,"hello"). MainPage has inherited the webdriver. This sets the value
    # x = search_text_element             #this invokes  __get__(self, MainPage_obj, MainPage). This gets the attribute

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)        # *(1,2) = 1, 2
        element.click()


class SearchResultsPage(BasePage):
    def is_results_found(self):
        return "No result found" not in self.driver.page_source