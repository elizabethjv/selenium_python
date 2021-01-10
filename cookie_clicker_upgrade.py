from selenium import webdriver #this is what opens up the browser. webdriver is the tool that links to the browser and does the necessary actions
from selenium.webdriver.common.keys import Keys  #access to common keys like Enter is imported
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe" #path to the chrome webdriver
driver = webdriver.Chrome(PATH)  #the chrome webdriver is linked to Chrome browser 
driver.get("https://orteil.dashnet.org/cookieclicker/")  #get to this url

driver.implicitly_wait(5)   #this wait is much more easier than the previous one using try catch

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice"+str(i))for i in range(1,-1,-1)]      #range starts at index 1 then steps down to 0, so the higher value available is stored first and that will be the one which will be bought

#Action chain is a pre-defined list of actions that we want to perform in a specific sequence. Queue of actions are stored. To perform it, use command actions.perform() 
actions = ActionChains(driver)   #new action chain object that will act on the webdriver
actions.click(cookie)     #adds click to the action chain queue

for i in range(5000):
    actions.perform()   #clicks the mouse at the cookie element
    count = int(cookie_count.text.split(" ")[0])   #  cookie_count.text is "5 cookies per second : 0", we just need to extract the initial number 
    
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)   #new action chain object is defined for the price item elements, with a new set of actions to perform on it
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()










# NOTES
#If class name is used to locate elements the webdriver returns the first element with that class name
#If id is not available, name is the next best thing, then class
# time.sleep(5)
# print(driver.title)
# print(driver.page_source) #scrapes the entire web page source code
# driver.close() #closes the current tab
# driver.quit()   #closes the browser window
# main.find_element_bylink_text("Submit")    #Helps to find an linked <a> or button element that has text on it eg. <a href='www.google.com'>Go to google</a> 
# driver.back()     #moves back or forward a page
# driver.forward()
# link.click()  #clicks the element if contains a link
# action.click() action.perform()  #clicks whereever the mouse is currently is


#Print all the search results titles
# country = driver.find_elements_by_class_name("Q8LRLc")
# search = driver.find_element_by_name("q")    #returns the search bar
# search.clear()  #clears any text in that input field
# search.send_keys("covid cases in "+country[0].text)        #send_keys() types the text into the element selected when a string is passed
# search.send_keys(Keys.RETURN)   #send_keys() executes the key passed
# try:
    # main = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "rso"))  #waits for the page to get loaded and returns the div element that contains all the search result
    # )
    # print(main.text)
    # articles = main.find_elements_by_class_name("g")  #returns all the search result div elements
    # for article in articles:
    #     header = article.find_elements_by_class_name("LC20lb DKV0Md")   #goes through each div and prints the text in the h2 tag
    #     print(header.text)
# except:
    # driver.quit() 

