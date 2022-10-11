from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")

driver = webdriver.Chrome(chrome_options=opt)

edit1 = driver.find_element_by_xpath('//*[@id="video-info-edit"]')
edit1.click()