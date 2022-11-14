from pytest_bdd import scenarios, given, then
from tests.helpers.helper import parse_custom
import requests

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

scenarios('../features/service.feature')


@given(parse_custom('the DuckDuckGo API is queried with "{phrase:str}"'), target_fixture='response')
def search(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


@then(parse_custom('the response status cose is "{code:num}"'))
def response_has_code(response, code):
    assert response.status_code == code


@then(parse_custom('the response contains results for "{phrase:str}"'))
def response_has_content(response, phrase):
    assert response.json()['Heading'].lower() == phrase.lower()
