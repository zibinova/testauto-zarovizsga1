from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(URL)

for _ in range(100):
    driver.find_element_by_id("submit").click()

iras = driver.find_elements_by_xpath('//li[contains(text(),"írás")]')

assert len(iras) >= 30

driver.close()
