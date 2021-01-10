#All CSS selectors are centralized to one location, so it will be very easy to change like the id name or attribute
#In this file, we create classes of the objects we want to find

from selenium.webdriver.common.by import By

#Define a class that has all of the locators for main page
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass



