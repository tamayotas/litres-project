import allure
from selene import browser, have


class ProfilePage:

    @allure.step('Verify profile user')
    def verify_profile_user_name(self, value):
        browser.element('[class*="Avatar-module__topContent"]').should(have.text(value))


user_profile = ProfilePage()
