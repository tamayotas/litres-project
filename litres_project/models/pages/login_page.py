import os

import allure
from dotenv import load_dotenv
from selene import browser, have


class LoginPage:
    @allure.step('Type login')
    def type_login(self):
        load_dotenv()
        login = os.getenv('USER_LOGIN')
        browser.element('[name="login"]').type(login)

    @allure.step('Type password')
    def type_password(self):
        load_dotenv()
        user_password = os.getenv('USER_PASSWORD')
        browser.element('#open_pwd_main').type(user_password).press_enter()

    @allure.step('Type wrong password')
    def type_wrong_password(self):
        load_dotenv()
        user_password = os.getenv('USER_WRONG_PASSWORD')
        browser.element('#open_pwd_main').type(user_password).press_enter()

    @allure.step('Check error message')
    def verify_error_message(self, value):
        browser.element('.err_text').should(have.text(value))


user_login = LoginPage()
