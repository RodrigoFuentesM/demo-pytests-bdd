import pytest
from pytest_bdd import given
from selenium import webdriver

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    yield browser
    browser.close()


@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)