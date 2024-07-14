import pytest
from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from utils.data import Order
import allure


class TestOrder:
    @pytest.mark.parametrize('user, button_order', [
        (Order.order_1, HomePageLocators.ORDER_HEADER),
        (Order.order_2, HomePageLocators.ORDER_PAGE)])
    def test_order(self, driver, user, button_order):
        if button_order == HomePageLocators.ORDER_HEADER:
            allure.dynamic.title('Проверка заказа самоката по кнопке "Заказать" в шапке')
        elif button_order == HomePageLocators.ORDER_PAGE:
            allure.dynamic.title('Проверка заказа самоката по кнопке "Заказать" в теле лендинга')
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        order_page.make_order(button_order)
        order_page.create_order_first(user[0], user[1], user[2], user[3])
        order_page.create_order_second(user[4])
        assert 'Заказ оформлен' in order_page.check_success_order()

