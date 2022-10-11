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
# username.send_keys('OA158241045')
# pwd.send_keys('Fap2yeah')

username.send_keys('OA158241043')
pwd.send_keys('Maydiputra0910')


sign_in_btn.click()
actions.pause(3)

myLearning = driver.find_element_by_xpath('//*[@id="main-menu"]/li[2]/a/span')
myCurrentLearning = driver.find_element_by_xpath('//*[@id="main-menu"]/li[1]/a')
myLearningHistory = driver.find_element_by_xpath('//*[@id="main-menu"]/li[2]/a')
myLearningPath = driver.find_element_by_xpath('//*[@id="main-menu"]/li[3]/a')

actions.move_to_element(myLearning).move_to_element(myCurrentLearning).move_to_element(myLearningHistory).move_to_element(myLearningPath).click().perform()

JavaProgramming = driver.find_element_by_link_text("JP Java Programming Learner - English")
JavaProgramming.click()

# !!!!!!!!!!!!!!!!!!!!!!!!!
# ISI DENGAN NAMA SECTION

courses = ["JP 2-3: Java Class Design - Abstract Classes", "JP 2-4: Exceptions and Assertions", "JP 3-1: Generics","JP 3-2: Collections - Part 1","JP 3-3: Collections - Part 2", "JP 3-4: Sorting and Searching", "JP 4-1: String Processing", "JP 4-2: Use Regular Expressions", "JP 4-3: Recursion", "JP 5-1: Basics of Input and Output", "JP 5-2: Input and Output Fundamentals", "JP 5-3: Deploying an Application", "JP 6-1: JDBC Introduction", "JP 6-2: JDBC Basics", "JP 7-1: Introduction to JVM Architecture", "JP 7-2: Java Memory Structure", "JP 8-1: JDK Tools", "JP 8-2: class File", "JP 9-1: Java Bytecode", "JP 9-2: ClassLoader"]

JF21= driver.find_element_by_link_text(courses[14])

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

# nextbtn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/nav/div[2]/button[2]')

nextbtn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/nav/div[2]/button[2]')

for i in range (0,100,+1) :
    nextbtn.click()
    time.sleep(3)