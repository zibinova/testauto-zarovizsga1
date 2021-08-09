from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(URL)

# defining fields:

a_field = driver.find_element_by_id("a")
b_field = driver.find_element_by_id("b")
calc_button = driver.find_element_by_id("submit")
result = driver.find_element_by_xpath("//span[@id='result']").get_attribute("value")
print(result)

# test data:

test_data_valid = [99, 12]
test_data_invalid = ["kiskutya", 12]
test_blank = ["", ""]


# calc function:


def calc(a, b):
    a_field.clear()
    b_field.clear()
    a_field.send_keys(a)
    b_field.send_keys(b)
    calc_button.click()
    res = (a + b) * 2
    return res


# TC 1: valid input data test:


assert calc(test_data_valid[0], test_data_valid[1]) == result

# TC 2: invalid input data test:
assert calc(test_data_invalid[0], test_data_valid[1]) == result

# TC 3: blank input data test:
assert calc(test_blank[0], test_blank[1]) == result
