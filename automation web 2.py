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
username.send_keys('OA91836730')
pwd.send_keys('Maydiputra0910')

sign_in_btn.click()
actions.pause(3)

myLearning = driver.find_element_by_xpath('//*[@id="main-menu"]/li[2]/a/span')
myCurrentLearning = driver.find_element_by_xpath('//*[@id="main-menu"]/li[1]/a')
myLearningHistory = driver.find_element_by_xpath('//*[@id="main-menu"]/li[2]/a')
myLearningPath = driver.find_element_by_xpath('//*[@id="main-menu"]/li[3]/a')

actions.move_to_element(myLearning).move_to_element(myCurrentLearning).move_to_element(myLearningHistory).move_to_element(myLearningPath).click().perform()

JavaProgramming = driver.find_element_by_link_text("PL/SQL Database Programming Learner - English")
JavaProgramming.click()

# !!!!!!!!!!!!!!!!!!!!!!!!!
# ISI DENGAN NAMA SECTION
sections = ["PL/SQL 2-2: Recognizing PL/SQL Lexical Units","PL/SQL 2-3: Recognizing Data Types","PL/SQL 2-4: Using Scalar Data Types","PL/SQL 2-5: Writing PL/SQL Executable Statements","PL/SQL 2-6: Nested Blocks and Variable Scope","PL/SQL 2-7: Good Programming Practices","PL/SQL Section 2 Quiz","PL/SQL 3-1: Review of SQL DML","PL/SQL 3-2: Retrieving Data in PL/SQL","PL/SQL 3-3: Manipulating Data in PL/SQL","PL/SQL 3-4: Using Transaction Control Statements","PL/SQL Section 3 Quiz","PL/SQL 4-1: Conditional Control: IF Statements","PL/SQL 4-2: Conditional Control: Case Statements","PL/SQL 4-3: Iterative Control: Basic Loops","PL/SQL 4-4: Iterative Control: WHILE and FOR Loops","PL/SQL 4-5: Iterative Control: Nested Loops","PL/SQL Section 4 Quiz","PL/SQL Database Programming Semester 1 Midterm Exam","PL/SQL 5-1: Introduction to Explicit Cursors","PL/SQL 5-2: Using Explicit Cursor Attributes","PL/SQL 5-3: Cursor FOR Loops","PL/SQL 5-4: Cursors with Parameters","PL/SQL 5-5: Using Cursors For Update","PL/SQL 5-6: Using Multiple Cursors","PL/SQL Section 5 Quiz","PL/SQL 6-1: User-Defined Records","PL/SQL 6-2: Indexing Tables of Records","PL/SQL Section 6 Quiz","PL/SQL 7-1: Handling Exceptions","PL/SQL 7-2: Trapping Oracle Server Exceptions","PL/SQL 7-3: Trapping User-Defined Exceptions","PL/SQL 7-4: Recognizing the Scope of Exceptions","PL/SQL Section 7 Quiz","PL/SQL 8-1: Creating Procedures","PL/SQL 8-2: Using Parameters in Procedures","PL/SQL 8-3: Passing Parameters","PL/SQL Section 8 Quiz","PL/SQL 9-1: Creating Functions","PL/SQL 9-2: Using Functions in SQL Statements","PL/SQL 9-3: Review of Data Dictionary","PL/SQL 9-4: Managing Procedures and Functions","PL/SQL 9-5: Review of Object Privileges","PL/SQL 9-6: Using Invoker's Rights and Autonomous Transactions","PL/SQL Section 9 Quiz","PL/SQL Database Programming Semester 1 Final Exam","PL/SQL 10-1: Creating Packages","PL/SQL 10-2: Managing Package Concepts","PL/SQL 10-3: Advanced Package Concepts","PL/SQL Section 10 Quiz","PL/SQL 11-1: Persistent State of Package Variables","PL/SQL 11-2: Using Oracle-Supplied Packages","PL/SQL Section 11 Quiz","PL/SQL 12-1: Using Dynamic SQL","PL/SQL 12-2: Improving PL/SQL Performance","PL/SQL Section 12 Quiz","PL/SQL Database Programming Semester 2 Midterm Exam","PL/SQL 13-1: Introduction to Triggers","PL/SQL 13-2: Creating DML Triggers: Part I","PL/SQL 13-3: Creating DML Triggers: Part II","PL/SQL 13-4: Creating DDL and Database Event Triggers","PL/SQL 13-5: Managing Triggers","PL/SQL Section 13 Quiz","PL/SQL 14-1: Introduction to Dependencies","PL/SQL 14-2: Understanding Remote Dependencies","PL/SQL Section 14 Quiz","PL/SQL 15-1: Using PL/SQL Initialization Parameters","PL/SQL 15-2: Displaying Compiler Warning Messages","PL/SQL 15-3: Using Conditional Compilation","PL/SQL 15-4: Hiding your Source Code"]

# print = sections[45]
JF21= driver.find_element_by_link_text(sections[59])
# print(len(sections))

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

for i in range (0,100,+1) :
    nextbtn.click()
    time.sleep(3)