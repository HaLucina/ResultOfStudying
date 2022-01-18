from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# driver path
driver_path = "C:\\hoge\\chromedriver.exe"

# URL of Google top
url = "https://www.google.co.jp/"

# Activation headless mode
options = Options()
#options.add_argument('--headless')

# open Google top
driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
driver.get(url)
sleep(2)

# Search for "python"
element = driver.find_element_by_name('q')
#element = driver.find_element_by_id("lst-ib")
#element = driver.find_element_by_class_name("gsfi")
element.send_keys("python")
element.submit()
sleep(5)

# close google chrome
driver.quit()
