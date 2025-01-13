from behave import given, when, then
from page_objects.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.driver.get("https://demo.opencart.com/index.php?route=account/login")
    context.login_page = LoginPage(context.driver)

@when('I enter email "{email}"')
def step_impl(context, email):
    context.login_page.input_text(*context.login_page.EMAIL_INPUT, email)

@when('I enter password "{password}"')
def step_impl(context, password):
    context.login_page.input_text(*context.login_page.PASSWORD_INPUT, password)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_element(*context.login_page.LOGIN_BUTTON)

@then('I should be logged in successfully')
def step_impl(context):
    assert "My Account" in context.driver.title

@then('I should see an error message')
def step_impl(context):
    assert "Warning: No match" in context.login_page.get_error_message()