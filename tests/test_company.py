from litres_project.models.pages.company_page import business_page
from litres_project.models.pages.home_page import main_page
import allure


@allure.label('UI')
@allure.epic('About company')
@allure.severity('critical')
@allure.title('Check about company page')
def test_about_company():
    main_page.open()

    main_page.navigate_to_about_company()

    business_page.verify_page_header('Сервис электронных книг №1 в России')
