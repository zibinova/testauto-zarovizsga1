from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)

email_field = driver.find_element_by_id("email")
submit_button = driver.find_element_by_id("submit")

# test data:

valid_email = "teszt@elek.hu"
invalid_email = "teszt@"
blank_email = ""


def fill_mail(email):
    email_field.clear()
    email_field.send_keys(email)
    submit_button.click()


# TC 1 test with valid email:


fill_mail(valid_email)
validation_error = driver.find_elements_by_class_name("validation-error")
assert len(validation_error) == 0

# TC 2 test with invalid email:

fill_mail(invalid_email)
validation_error = driver.find_element_by_class_name("validation-error")
expected_message = "Please enter a part following '@'. 'teszt@' is incomplete."
assert validation_error.text == expected_message

# TC 3 test with blank email:

fill_mail(blank_email)
validation_error = driver.find_element_by_class_name("validation-error")
expected_message = "Please fill out this field."
assert validation_error.text == expected_message


# 14 pont