import allure
from selene import browser, have


class CompanyPage:

    @allure.step('Verify page header should be {value}')
    def verify_page_header(self, value):
        browser.all('.main-section>h2').first.should(have.text(value))


business_page = CompanyPage()
