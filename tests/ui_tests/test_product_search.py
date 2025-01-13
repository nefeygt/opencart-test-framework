import pytest
from page_objects.search_page import SearchPage

class TestProductSearch:
    @pytest.mark.ui
    def test_search_existing_product(self, driver):
        search_page = SearchPage(driver)
        driver.get("https://demo.opencart.com")
        search_page.search_product("iPhone")
        results = search_page.get_search_results()
        assert any("iPhone" in result for result in results)

    @pytest.mark.ui
    def test_search_with_filters(self, driver):
        search_page = SearchPage(driver)
        driver.get("https://demo.opencart.com")
        search_page.search_product("iPhone")
        search_page.apply_filter("category", "Phones & PDAs")
        results = search_page.get_search_results()
        assert len(results) > 0