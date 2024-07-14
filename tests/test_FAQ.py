from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from conftest import driver
from utils.data import HomePageFAQ
import pytest
import allure


class TestQuestionsHomePage:
    @allure.title('Проверка соответствия ответов в выпадающих списках раздела "Вопросы о важном"')
    @pytest.mark.parametrize('number, expected_answer', HomePageFAQ.answers)
    def test_question(self, driver, number, expected_answer):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.scroll(HomePageLocators.LAST_QUESTION)
        home_page.click_question(number)
        assert home_page.get_answer(number) == expected_answer
