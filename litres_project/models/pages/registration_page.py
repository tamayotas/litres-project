import os
import allure
from selene import browser, have
from dotenv import load_dotenv


class RegistrationPage:

    @allure.step('Open registration page')
    def open_registration_page(self):
        browser.open('/pages/registration/')

    @allure.step('Type new register email')
    def type_new_register_email(self):
        load_dotenv()
        new_register_email = os.getenv('REGISTER_USER')
        browser.element('[name="email"]').type(new_register_email).press_enter()

    @allure.step('Type existing email')
    def type_existing_email(self):
        load_dotenv()
        register_email = os.getenv('USER_LOGIN')
        browser.element('[name="new_login"]').type(register_email)

    @allure.step('Type register password')
    def type_password(self):
        load_dotenv()
        register_password = os.getenv('USER_PASSWORD')
        browser.element('[name="new_pwd_open"]').type(register_password).press_enter()

    @allure.step('Verify profile can be created')
    def should_can_create_profile(self, value):
        browser.element('[data-testid="authorization-popup"] [class*="EmailMessage"]').should(have.text(value))

    @allure.step('Verify profile can not be created')
    def should_cannot_create_profile(self, value):
        browser.element('.err_text').should(have.text(value))


reg_page = RegistrationPage()
