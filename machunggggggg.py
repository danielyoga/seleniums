from os import add_dll_directory
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://mahasiswa.machung.ac.id/')
actions = ActionChains(driver)

username = driver.find_element_by_xpath('//*[@id="inputEmail"]')
username.send_keys('311910006')

passwordd = driver.find_element_by_xpath('//*[@id="inputPassword"]')
passwordd.send_keys('Maydiputra0910')

sign_in_btn = driver.find_element_by_xpath('/html/body/div/div/div/form/button')
sign_in_btn.click()

print("SUDAH")