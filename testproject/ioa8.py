from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(URL)

driver.find_element_by_id("submit").click()

num1 = driver.find_element_by_id("num1").text
print(num1)
operator = driver.find_element_by_id("op").text
print(operator)
num2 = driver.find_element_by_id("num2").text
print(num2)
result = driver.find_element_by_id("result").text
result = int(result)

if operator == "+":
    res = int(num1)+int(num2)
elif operator == "-":
    res = int(num1)-int(num2)
elif operator == "*":
    res = int(num1) * int(num2)
else:
    res = int(num1) // int(num2)
assert result == res

driver.close()


# 16 pont max

