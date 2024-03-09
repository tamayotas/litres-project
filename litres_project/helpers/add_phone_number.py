from selene import browser, be, have
import os


def skip_phone_number():
    base_url = os.getenv('BASE_URL')
    browser.should(have.url_containing(base_url))
    browser.driver.refresh()
    if browser.element('[data-testid="authorization-popup"]').matching(be.visible):
        browser.element('[data-testid="authorization-popup__close-button"]').should(
            be.visible).click()
