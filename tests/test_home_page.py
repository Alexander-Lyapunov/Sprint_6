from conftest import driver
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from utils.urls import Urls
import allure


class TestLogo:
    @allure.title('Проверка перехода на главную страницу сайта при клике на Самокат в лого шапки')
    def test_redirect_samokat_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_to_element(HomePageLocators.ORDER_HEADER)
        home_page.click_samokat_logo()
        home_page.wait_url(Urls.SAMOKAT_PAGE_URL)
        assert Urls.SAMOKAT_PAGE_URL == home_page.get_current_url()

    @allure.title('Проверка перехода на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_yandex_logo()
        home_page.tab_switch()
        home_page.wait_url(Urls.DZEN_PAGE_URL)
        assert Urls.DZEN_PAGE_URL == home_page.get_current_url()
