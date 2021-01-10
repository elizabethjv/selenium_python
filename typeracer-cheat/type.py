import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait

def run():

    chrome_driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
    chrome_driver.get("https://play.typeracer.com/")

    start_wait = WebDriverWait(chrome_driver,30)

    start_button = start_wait.until(
        element_to_be_clickable((By.XPATH, "//A[contains(.,'Enter a typing race)"))
    )

    start_button.click()

    race_text = get_race_text(chrome_driver)

    type_wait = WebDriverWait(chrome_driver,30)

    typing_area = type_wait.until(
        element_to_be_clickable((By.XPATH, "//input[@class='txtInput']"))
    )

    for letter in race_text:
        typing_area.send_keys(letter)
        delay = 0.002
        time.sleep(delay)

    time.sleep(100000)

def get_race_text(driver):
    wait = WebDriverWait(driver,30)

    text_elements = wait.until(
        presence_of_all_elements_located((By.XPATH, "//span[@unselectable='on']"))
    )

    text_parts = [el.text for el in text_elements]

    race_text = ''
    if len(text_parts) == 3:
        race_text = '{}{} {}'.format(text_parts[0], text_parts[1], text_parts[2])
    elif len(text_parts) == 2:
        race_text = '{} {}'.format(text_parts[0], text_parts[1])
    return race_text


if __name__ == '__main__':
    run()