from behave import given, when, then
from page_objects.search_page import SearchPage

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("https://demo.opencart.com")
    context.search_page = SearchPage(context.driver)

@when('I search for "{product}"')
def step_impl(context, product):
    context.search_page.search_product(product)

@then('I should see "{product}" in the search results')
def step_impl(context, product):
    results = context.search_page.get_search_results()
    assert any(product.lower() in result.lower() for result in results)