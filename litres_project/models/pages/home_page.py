import allure
from selene import browser, have


class HomePage:
    @allure.step('Open main page')
    def open(self):
        browser.open('/')

    @allure.step('Open profile')
    def open_profile(self):
        browser.open('/pages/login/')

    @allure.step('Navigate to login tab')
    def navigate_to_login_tab(self):
        browser.element('[data-testid="tab-login"]').click()

    @allure.step('Verify profile button text and click it')
    def verify_text_profile_button(self, value):
        browser.element('[data-testid="header__profile-button"] [class*="Button__title"]').should(have.text(value))
        browser.element('[data-testid="header__profile-button"]').click()

    @allure.step('Navigate to about company and click it')
    def navigate_to_about_company(self):
        browser.element('[href="/o-kompanii/"]').click()

    @allure.step('Search book by value')
    def search_book(self, value):
        browser.element('[name="q"]').type(value)
        browser.element('[type="submit"]').click()


main_page = HomePage()
