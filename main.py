from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pandas as pd


driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = 'C:/Users/Irshad Khatri/Downloads/chromedriver-win64'
def create_webdriver():
    return webdriver.Chrome()

browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")
