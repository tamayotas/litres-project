import allure
from selene import browser, have


class SearchPage:

    @allure.step('Verify search page')
    def verify_search_page(self, value):
        browser.element('[data-testid="search-title__wrapper"]').should(have.text(value))

    @allure.step('Verify not found search data')
    def verify_not_found_search_data(self, value):
        browser.element('[data-testid="search-title__wrapper"]').should(have.text(value))


search_instance = SearchPage()
