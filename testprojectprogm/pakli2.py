from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f2.html"

driver.get(URL)


def find_all_cards():
    return driver.find_elements_by_xpath('//div[@class="card"]')


test_data = [(True, ), (0, ), (52, "9", 4)]

submit_button = driver.find_element_by_id("submit")
card_list = find_all_cards()


def test_initial_submit_enabled():
    assert submit_button.is_enabled() == test_data[0][0]


def test_initial_card_list_empty():
    assert len(card_list) == test_data[1][0]


def test_proper_card_deck():
    for _ in range(test_data[2][0]):
        submit_button.click()
    current_card_list = find_all_cards()
    niners = 0
    for card in current_card_list:
        if test_data[2][1] in card.text:
            niners += 1

    assert niners == test_data[2][2]


test_initial_submit_enabled()
test_initial_card_list_empty()
test_proper_card_deck()
