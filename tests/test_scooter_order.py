from pages.homepage import Homepage
from pages.scooter_order_page import ScooterOrderPage
from data import URLs, OrderDataSets
import pytest
import allure


class TestScooterOrder:

    @allure.title('Заказ самоката')
    @pytest.mark.parametrize('data_set', OrderDataSets.data_set_list)
    @pytest.mark.parametrize('button', [Homepage.top_order_button, Homepage.bottom_order_button])
    def test_scooter_order(self, driver, data_set, button):

        order = ScooterOrderPage(driver)
        order.go_to_page(URLs.base_url)
        order.click_order_button(button)
        order.fill_order_form(data_set)

        order.check_popup_success_order()
