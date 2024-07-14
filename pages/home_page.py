from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure
from utils.urls import Urls


class HomePage(BasePage):
    @allure.step('Клик на вопрос')
    def click_question(self, number):
        method, locator = HomePageLocators.QUESTION_LIST
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.click_to_element((method, locator))

    @allure.step('Получение ответа')
    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER_LIST
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.get_text((method, locator))

    @allure.step('Клик на Яндекс в шапке')
    def click_yandex_logo(self):
        self.click_to_element(HomePageLocators.LOGO_YANDEX)

    @allure.step('Клик на Самокат в шапке')
    def click_samokat_logo(self):
        self.click_to_element(HomePageLocators.LOGO_SAMOKAT)

    @allure.step('Открываем сайт "Яндекс.Самокат"')
    def open_home_page(self):
        self.open_url(Urls.SAMOKAT_PAGE_URL)
        self.wait_element(HomePageLocators.COOKIES_BUTTON)
        self.get_cookies(HomePageLocators.COOKIES_BUTTON)
