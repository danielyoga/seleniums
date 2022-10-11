from os import add_dll_directory
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://myacademy.oracle.com/lmt/xlr8login.login?site=oa')
actions = ActionChains(driver)

username = driver.find_element_by_xpath('//*[@id="inputUsername"]')
pwd = driver.find_element_by_xpath('//*[@id="inputPassword"]')
sign_in_btn = driver.find_element_by_xpath('//*[@id="login-page"]/div[2]/form/div/ul[3]/li/input')

# !!!!!!!!!!!!!!!!!!!!!!!!!
# ISI USERNAME DAN PASSWORD
username.send_keys('OA91836727')
pwd.send_keys('Fap2yeah')

sign_in_btn.click()
time.sleep(5)

# !!!!!!!!!!!!!!!!!!!!!!!!!!
# WRITE COURSES HERE

kelas = driver.find_element_by_xpath('//*[@id="scrollBodyTableDiv"]/div[1]/div[1]/div[2]/dl/dt')

kelas.click()
time.sleep(5)

course = driver.find_element_by_xpath('/html/body/div/main/section[3]/div/div/section/div[2]/div[3]/div/div[2]/h4')
course.click()

# !!!!
# LOOP
courses = ['PL/SQL 2-1: Using Variables in PL/SQL',
'PL/SQL 2-2: Recognizing PL/SQL Lexical Units',
'PL/SQL 2-3: Recognizing Data Types',
'PL/SQL 2-4: Using Scalar Data Types',
'PL/SQL 2-5: Writing PL/SQL Executable Statements',
'PL/SQL 2-6: Nested Blocks and Variable Scope',
'PL/SQL 2-7: Good Programming Practices]',]

PL1 = driver.find_element_by_link_text(courses[5])
PL1.click()

Play = driver.find_element_by_link_text("Play")
Play.click()

time.sleep(4)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.switch_to.window(driver.window_handles[1])
print("Window switch")

driver.switch_to.frame(driver.find_element_by_css_selector('#content-iframe'))
print("frame switch")

time.sleep(5)

# No = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[2]/div/button[2]')

# No.click()

nextbtn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/nav/div[2]/button[2]')

for i in range (0,50,+1) :
    nextbtn.click()
    time.sleep(3)