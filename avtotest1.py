from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = 'https://www.youtube.com/'
time.sleep(3)
browser = webdriver.Chrome()
time.sleep(3)
browser.get(link)
time.sleep(3)
#


button = browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]").click()
time.sleep(3)

serch_string = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
serch_string.send_keys("savchukyuriy81@gmail.com")

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# link = 'https://www.youtube.com/'
# browser = webdriver.Chrome()
# browser.get(link)





