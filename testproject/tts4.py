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
print(len(iras))

assert len(iras) >= 30

driver.close()
# 14 pont


# sol:
#
# number_of_heads = 0
# for i in range(1, 101):
#     cf_button.click()
#     # result = driver.find_element_by_xpath(f'//*[@id="results"]/li[{i}]').text
#     result = driver.find_element_by_id("lastResult").text
#     if result == "fej":
#         number_of_heads += 1
# print(number_of_heads)
#
# # A számlálónlnak minimum 30-nak kell lennie
# assert number_of_heads >= 30