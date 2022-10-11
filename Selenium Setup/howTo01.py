from selenium import webdriver
# PATH = "C:\Program Files (x86)\msedgedriver.exe"
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
# driver = webdriver.Edge(PATH)
# driver.get("https://studio.youtube.com/channel/UC79qe7FNEatrTznOZlXABnQ/livestreaming")
driver.get("https://www.youtube.com")

