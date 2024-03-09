import allure

from litres_project.helpers.add_phone_number import skip_phone_number
from litres_project.models.pages.home_page import main_page
from litres_project.models.pages.login_page import user_login
from litres_project.models.pages.profile_page import user_profile


@allure.epic('Authorization')
class TestLogin:

    @allure.label('UI')
    @allure.epic('Authorization')
    @allure.severity('critical')
    @allure.title('Successful login user')
    def test_successful_login_user(self):
        main_page.open_profile()

        user_login.type_login()
        user_login.type_password()
        skip_phone_number()

        main_page.verify_text_profile_button('Профиль')
        user_profile.verify_profile_user_name('autotest selene')

    @allure.label('UI')
    @allure.epic('Authorization')
    @allure.severity('minor')
    @allure.title('Unsuccessful login user')
    def test_unsuccessful_login(self):
        main_page.open_profile()

        user_login.type_login()
        user_login.type_wrong_password()

        user_login.verify_error_message('Логин невозможен (неверное сочетание логина и пароля)')
