from pages.base_page import BasePage
from data import URLs
from selenium.webdriver.common.by import By
import allure


class ScooterOrderPage(BasePage):

    next_button = (By.XPATH, './/button[text()="Далее"]')
    form_order_button = (By.XPATH, './/div[contains(@class,"Order_Content")]//button[text()="Заказать"]')

    name = (By.XPATH, './/input[@placeholder="* Имя"]')
    surname = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    address = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    subway_station_list = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    subway_station = (By.XPATH, './/li[@data-index="5"]')
    phone_number = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    date = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    rent_period = (By.XPATH, './/div[text()="* Срок аренды"]/following::span')
    period = (By.XPATH, './/div[text()="трое суток"]')
    color = (By.ID, 'black')
    comment = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    submit_order_button = (By.XPATH, './/div[text()="Хотите оформить заказ?"]/following::button[text()="Да"]')
    order_modal = (By.XPATH, './/div[contains(@class,"Order_ModalHeader")]')

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_visible_element(locator)
        self.wait_url_to_be(URLs.order_url)

    @allure.step('Заполняем форму заказа')
    def fill_order_form(self, data_set):
        self.send_keys_to_element(self.name, data_set['name'])
        self.send_keys_to_element(self.surname, data_set['surname'])
        self.send_keys_to_element(self.address, data_set['address'])
        self.click_visible_element(self.subway_station_list)
        self.click_visible_element(self.subway_station)
        self.send_keys_to_element(self.phone_number, data_set['phone_number'])
        self.click_visible_element(self.next_button)
        self.send_keys_to_element(self.date, data_set['date'])
        self.click_visible_element(self.date)
        self.click_visible_element(self.rent_period)
        self.click_visible_element(self.period)
        self.click_visible_element(self.color)
        self.send_keys_to_element(self.comment, data_set['comment'])
        self.click_visible_element(self.form_order_button)
        self.click_visible_element(self.submit_order_button)

    def get_order_modal_text(self):
        return self.find_visible_element(self.order_modal).text

    @allure.step('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_popup_success_order(self):
        assert 'Заказ оформлен' in self.get_order_modal_text()
