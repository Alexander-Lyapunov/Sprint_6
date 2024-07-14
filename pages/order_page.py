from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    @allure.step('Жмем на кнопку "Заказать"')
    def make_order(self, button_order):
        self.click_to_element(button_order)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.FIELD_NAME, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.FIELD_LAST_NAME, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step('Выбор станции метро')
    def set_metro(self):
        self.click_to_element(OrderPageLocators.FIELD_METRO)
        self.action_arrowdown()
        self.action_enter()

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_ORDER)

    @allure.step('Заполнение формы "Для кого самокат"')
    def create_order_first(self, name, last_name, address, phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro()
        self.set_phone(phone)
        self.click_next_button()

    @allure.step('Выбор даты доставки')
    def set_date(self):
        self.click_to_element(OrderPageLocators.FIELD_DATE)
        self.action_arrowdown()
        self.action_enter()

    @allure.step('Выбор продолжительности срока аренды')
    def set_period_rent(self):
        self.click_to_element(OrderPageLocators.FIELD_PERIOD_RENT)
        self.click_to_element(OrderPageLocators.RENT_PERIOD_DAY)

    @allure.step('Выбор цвета')
    def set_color(self):
        self.click_to_element(OrderPageLocators.BLACK_SAMOKAT)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.FIELD_COMMENT, comments)

    @allure.step('Заполнение формы "Про аренду"')
    def create_order_second(self, comments):
        self.set_date()
        self.set_period_rent()
        self.set_color()
        self.set_comments(comments)
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Появление всплывающего окна "Заказ оформлен"')
    def check_success_order(self):
        return self.find_element(OrderPageLocators.ORDER_SUCCESS).text
