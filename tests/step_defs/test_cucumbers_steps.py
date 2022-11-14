from pytest_bdd import scenarios, given, when, then
from cucumbers import CucumberBasket
from tests.helpers.helper import parse_custom

scenarios('../features/cucumbers.feature')


@given(parse_custom('the basket has "{initial:num}" cucumbers'), target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parse_custom('"{some:num}" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parse_custom('"{some:num}" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parse_custom('the basket contains "{total:num}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total
