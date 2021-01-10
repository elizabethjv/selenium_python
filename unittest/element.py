#This file represents one element on the page. Eg represent a search bar or form input
#This allows for easy way to change the element

from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    #To set the value on an element in the page
    def __set__(self,obj,value):   #Dunder method: sets the attribute on an instance of the class passed to a new value
        driver = obj.driver        #webdriver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator)      # lambda is an anonymous function. Syntax: lambda arguments : expression. Wait until this function is true
        )
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    #To get the value on an element in the page
    #This function allows us to access attributes without waiting for 5 secs. Just a .__get__(obj_name, owner_class_name) would return the attribute
    def __get__(self,obj,owner):   #Dunder method: Called to get the attribute of an instance of that class.
        driver = obj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator)      # lambda is an anonymous function
        )
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")           #get_attribute method is used to get attributes of an element, such as getting href attribute of anchor tag. get_arrtribute("value") returns the attribute of that specific value
