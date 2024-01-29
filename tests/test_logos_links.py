from data import URLs
from pages.homepage import Homepage
import allure


class TestLogosLinks:

    @allure.title('Проверяем, если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_scooter_logo_open_homepage(self, driver):

        logo = Homepage(driver)
        logo.go_to_page(URLs.order_url)
        logo.click_visible_element(logo.scooter_logo)

        assert logo.current_page() == URLs.base_url

    @allure.title('Проверяем, если нажать на логотип Яндекса, в новом окне откроется главная страница Дзена')
    def test_yandex_logo_open_dzen(self, driver):

        logo = Homepage(driver)
        logo.go_to_page(URLs.base_url)
        logo.click_visible_element(logo.yandex_logo)
        logo.switch_to_new_window()
        logo.wait_url_contain('http')
        logo.wait_url_not_contain('passport')

        assert URLs.dzen_url in logo.current_page()
