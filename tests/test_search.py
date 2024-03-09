from litres_project.models.pages.home_page import main_page
from litres_project.models.pages.search_page import search_instance
import allure


@allure.story('Search')
class TestSearch:

    @allure.label('UI')
    @allure.epic('Search')
    @allure.severity('major')
    @allure.title('Search available book')
    def test_search_available_book(self):

        main_page.open()

        main_page.search_book('стивен кинг')

        search_instance.verify_search_page('Результаты поиска «стивен кинг»')

    @allure.label('UI')
    @allure.epic('Search')
    @allure.severity('trivial')
    @allure.title('Search not available book')
    def test_search_not_available_book(self):

        main_page.open()

        main_page.search_book('python testing with pytest')

        search_instance.verify_not_found_search_data('ничего не найдено')
