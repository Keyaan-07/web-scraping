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


projects = browser.find_elements("xpath", "//h1[@class='h3 lh-condensed']")

project_list = {}
for proj in projects:
    proj_name = proj.text # Project name
    proj_url = proj.find_elements("xpath", "a")[0].get_attribute('href') # Project URL
    project_list[proj_name] = proj_url

browser.quit()

project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)

project_df.to_excel('project_list.xlsx')
