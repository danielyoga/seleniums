from os import add_dll_directory
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome()
driver.get('https://myacademy.oracle.com/lmt/xlr8login.login?site=oa')
actions = ActionChains(driver)

username = driver.find_element_by_xpath('//*[@id="inputUsername"]')
pwd = driver.find_element_by_xpath('//*[@id="inputPassword"]')
sign_in_btn = driver.find_element_by_xpath('//*[@id="login-page"]/div[2]/form/div/ul[3]/li/input')

# !!!!!!!!!!!!!!!!!!!!!!!!!
# ISI USERNAME DAN PASSWORD
username.send_keys('OA158241043')
pwd.send_keys('Maydiputra0910')

sign_in_btn.click()
actions.pause(3)

myLearning = driver.find_element_by_xpath('//*[@id="main-menu"]/li[2]/a/span')
myCurrentLearning = driver.find_element_by_xpath('//*[@id="main-menu"]/li[1]/a')
myLearningHistory = driver.find_element_by_xpath('//*[@id="main-menu"]/li[2]/a')
myLearningPath = driver.find_element_by_xpath('//*[@id="main-menu"]/li[3]/a')

actions.move_to_element(myLearning).move_to_element(myCurrentLearning).move_to_element(myLearningHistory).move_to_element(myLearningPath).click().perform()

# JavaProgramming = driver.find_element_by_link_text("JP Java Programming Learner - English")
JavaProgramming = driver.find_element_by_link_text("JF Java Fundamentals Learner - English")
JavaProgramming.click()

# !!!!!!!!!!!!!!!!!!!!!!!!!
# ISI DENGAN NAMA SECTION
JF21= driver.find_element_by_link_text("JF 3-5: Randomization and Understanding Dot Notation and Constructors")

JF21.click()

Play = driver.find_element_by_link_text("Play")

Play.click()

print(driver.current_window_handle)
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.switch_to.window(driver.window_handles[1])
print("Window switch")

driver.switch_to.frame(driver.find_element_by_css_selector('#content-iframe'))
print("frame switch")

time.sleep(5)

No = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[2]/div/button[2]')

No.click()

nextbtn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/nav/div[2]/button[2]')

for i in range (0,50,+1) :
    nextbtn.click()
    time.sleep(3)