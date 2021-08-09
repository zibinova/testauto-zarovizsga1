from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)

city_input_field = driver.find_element_by_id("missingCity")
submit_button = driver.find_element_by_id("submit")

result_message = driver.find_element_by_id("result").text
print(result_message)

# a varosokat listaba kene torni, vegigiteralni rajtuk for ciklussal, berakni oket a city input field mezobe
# megvizsgalni if feltetellel hogy submit utan mi a message
# ha emberibb idoben probalkoznek,talan tobbre mennek kicsivel, de azert nagyon koszonom a lehetoseget

cities = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford",
          "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis",
          "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston",
          "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City",
          "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City",
          "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City",
          "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]


def city_guess():
    city_input_field.clear()
    city_input_field.send_keys(city)
    submit_button.click()


for city in cities:
    city_guess()
    if result_message != "Nem találtad el.":
        break
