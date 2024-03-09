import allure

from litres_project.models.pages.home_page import main_page
from litres_project.models.pages.registration_page import reg_page


@allure.epic('Registration')
class TestRegistration:

    @allure.label('UI')
    @allure.epic('Registration')
    @allure.severity('critical')
    @allure.title('User can be registered successfully')
    def test_registration_user(self):
        main_page.open()
        main_page.navigate_to_login_tab()

        reg_page.type_new_register_email()

        reg_page.should_can_create_profile('Адрес свободен для регистрации')

    @allure.tag('UI')
    @allure.epic('Registration')
    @allure.severity('critical')
    @allure.title('User cannot be registered with existing email')
    def test_registration_user_with_existing_email(self):
        reg_page.open_registration_page()

        reg_page.type_existing_email()
        reg_page.type_password()

        reg_page.should_cannot_create_profile('Карта привязана к аккаунту другого пользователя')
