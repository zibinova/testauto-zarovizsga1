from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f4.html"

driver.get(URL)
time.sleep(2)


def find_loc(id):
    return driver.find_element_by_id(id)


submit_button = driver.find_element_by_xpath('/html/body/div[1]/form/input[3]')

test_data_1 = ["teszt@elek.hu", "Kiscica1234"]
test_data_2 = ["teszt@elek.hu", "a1"]


# TC1-helyes kitöltés
def test_tc1():
    find_loc("usrname").send_keys(test_data_1[0])
    find_loc("psw").send_keys(test_data_1[1])
    submit_button.click()
    time.sleep(2)
    assert find_loc("titleText").text == "404: Not Found"


# TC2-helytelen kitöltés
def test_tc2():
    driver.get(URL)
    find_loc("usrname").send_keys(test_data_2[0])
    find_loc("psw").send_keys(test_data_2[1])

    assert find_loc("message").is_displayed()
    assert find_loc("number").get_attribute("class") and find_loc("letter").get_attribute("class") == "valid"
    assert find_loc("capital").get_attribute("class") and find_loc("length").get_attribute("class") == "invalid"

    driver.quit()


# """első verzió:
# def test_tc1():
#     """Helyes kitöltés esete:
#         email: teszt@elek.hu
#         jelszó: Kiscica1234
#         A Submit gomb megnyomása után átnavigál egy oldalra ahol a "404 Not Found" hibaüzenet látható."""
#
#     username = driver.find_element_by_id("usrname")
#     username.send_keys("teszt@elek.hu")
#     password = driver.find_element_by_id("psw")
#     password.send_keys("Kiscica1234")
#
#     submit_button = driver.find_element_by_xpath("/html/body/div[1]/form/input[3]")
#     submit_button.click()
#
#     error_message = driver.find_element_by_id("titleText").text
#     assert error_message == "404: Not Found"
#
#
# def test_tc2():
#     """Helytelen kitöltés esete:
#         email: teszt@elek.hu
#         jelszó: a1"""

#     driver.get(URL)
#     username = driver.find_element_by_id("usrname")
#     username.send_keys("teszt@elek.hu")
#     password = driver.find_element_by_id("psw")
#     password.send_keys("a1")
#
#     submit_button = driver.find_element_by_xpath("/html/body/div[1]/form/input[3]")
#     submit_button.click()
#
#     val_el = driver.find_elements_by_class_name("valid")
#     # print(len(val_el))
#     valid_element = []
#     for el in val_el:
#         valid_element.append(el.text)
#     # print(valid_element)
#     assert valid_element == ['A lowercase letter', 'A number']"""
