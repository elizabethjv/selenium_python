import unittest
from selenium import webdriver
import page

#The class is the main test case and within it, the methods are little tests cases inside it
class PythonOrgSearch(unittest.TestCase):    #inherits the class TestCase
    #this method always runs first when the test case starts
    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.python.org")


    def test_search_python(self):
        mainPage = page.MainPage(self.driver)      #creates the object for the class defined in page.py
        assert mainPage.is_title_matches()         #if the assertion is true do the next lines
        mainPage.search_text_element = "pycon"       #invokes the __set__
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()

    #this method always runs last when the test cases are over  
    def tearDown(self):
        self.driver.close()

#if this main.py is run, not if its imported,  run all the unittests defined
if __name__ == "__main__":
    unittest.main()





    # #since TestCase is inherited, if we start any method with keyword "test" it will automatically run when the unittest is run 
    # #setUp and tearDown are called during each of the testcase methods
    # def test_example(self):
    #     print("Test")
    #     assert False    #assert checks if the condition on its RHS in this case "True" is true. This is the way we can tell if a test case failed or pass

    # def test_example_2(self):
    #     assert True