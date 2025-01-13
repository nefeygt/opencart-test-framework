Feature: User Login
    As a registered customer
    I want to log into my account
    So that I can access my personal account area

    Scenario: Successful login with valid credentials
        Given I am on the login page
        When I enter email "demo@opencart.com"
        And I enter password "demo123"
        And I click the login button
        Then I should be logged in successfully

    Scenario: Failed login with invalid credentials
        Given I am on the login page
        When I enter email "wrong@email.com"
        And I enter password "wrongpass"
        And I click the login button
        Then I should see an error message