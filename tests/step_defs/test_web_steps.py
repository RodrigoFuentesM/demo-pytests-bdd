from pytest_bdd import given, scenarios, when, then, parsers
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

scenarios('../features/web.feature')


# @pytest.fixture
# def browser():
#     browser = webdriver.Firefox()
#     browser.implicitly_wait(10)
#     yield browser
#     browser.close()
#
#
# @given('the DuckDuckGo home page is displayed')
# def ddg_home(browser):
#     browser.get(DUCKDUCKGO_HOME)


@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys(text + Keys.RETURN)


@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements(By.XPATH, xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element(By.ID, 'links')
    assert len(links_div.find_elements(By.XPATH, '//div')) > 0
    search_input = browser.find_element(By.NAME, 'q')
    assert search_input.get_attribute('value') == phrase
