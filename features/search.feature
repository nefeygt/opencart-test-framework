Feature: Product Search
    As a customer
    I want to search for products
    So that I can find items I want to purchase

    Scenario: Search for existing product
        Given I am on the homepage
        When I search for "iPhone"
        Then I should see "iPhone" in the search results

    Scenario: Search for non-existing product
        Given I am on the homepage
        When I search for "nonexistentproduct123"
        Then I should see "No products found" message