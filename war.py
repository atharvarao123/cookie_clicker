from ast import Return
import imp
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\\users\\athar\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")


while True:
    cookie.click()
    if(cookie_count.text.split(" ")[0] == "25"):
        cursoe = driver.find_element_by_id("product0")
        cursoe.click()
    elif(cookie_count.text.split(" ")[0] == "300"):
        cursoe = driver.find_element_by_id("product1")
        cursoe.click()
  
    


