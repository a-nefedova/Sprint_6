import allure

from pages.scooter_order_page import ScooterOrderPage
from data import URLs, OrderDataSets
import pytest


class TestScooterOrder:

    @allure.title('Заказ самоката')
    @pytest.mark.parametrize('data_set', OrderDataSets.data_set_list)
    @pytest.mark.parametrize('button', [ScooterOrderPage.top_order_button, ScooterOrderPage.bottom_order_button])
    def test_scooter_order(self, driver, data_set, button):

        order = ScooterOrderPage(driver)
        order.go_to_page(URLs.base_url)
        order.click_order_button(button)
        order.fill_order_form(data_set)

        order.check_popup_success_order()
        order.check_scooter_logo_open_homepage()
        order.check_yandex_logo_open_dzen()
