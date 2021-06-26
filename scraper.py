from selenium import webdriver
import time
import math

num1 = 220352179
num2 = 222817224
url = 'https://platform.virdocs.com/r/s/0/doc/1759843/sp/'
url2 = 'https://platform.virdocs.com/r/s/0/doc/1772670/sp/'
#set chromodriver.exe path
driver = webdriver.Chrome(executable_path='C:\\Users\\Kunal\\Documents\\GitHub\\Redshelf_webscraper\\chromedriver.exe')
driver.maximize_window()
driver.get("https://canvas.ucsd.edu")
time.sleep(3)
driver.find_element_by_id("ssousername").send_keys("INSERTUSERNAME")
driver.find_element_by_id("ssopassword").send_keys("INSERTPASSWORD")
time.sleep(1)
driver.find_element_by_class_name("sso-button").click()
time.sleep(20)
#launch URL
driver.get("https://canvas.ucsd.edu/courses/26782/modules/items/818638")
time.sleep(1)
driver.get("https://ucsandiegobookstore.redshelf.com/course/course_details/240830/")
time.sleep(1)
textbookID_1 = "1692267"
textbookID_2 = "238740"
workbookID_1 = "1703206"
workbookID_2 = "240830"
driver.get("https://ucsandiegobookstore.redshelf.com/book/read/" + workbookID_1 + "/?course_id=" + workbookID_2)
time.sleep(3)
driver.get(url2+str(num2))
time.sleep(6)
#get window size
s = driver.get_window_size()
#obtain browser height and width
w = driver.execute_script('return document.body.parentNode.scrollWidth')
h = driver.execute_script('return document.body.parentNode.scrollHeight')
#set to new window size
driver.set_window_size(w-450, h+920)
#obtain screenshot of page within body tag
numPages = 382
i = 0
while (num2+i) != 222817232:
    driver.find_element_by_tag_name('iframe').screenshot("images2\\page_" + str(i+1) + ".png")
    driver.find_element_by_class_name("spine-entry-nav-container-next").click()
    i += 1
    time.sleep(1.56)
# filename = 'screenshot1.png'
# driver.set_window_size(1280,800)
# save_fullpage_screenshot(driver, url+str(num), "images\\" + filename)
driver.set_window_size(s['width'], s['height'])
driver.quit()


