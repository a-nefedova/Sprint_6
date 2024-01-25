from pages.base_page import BasePage
from data import URLs
from selenium.webdriver.common.by import By
import allure


class ScooterOrderPage(BasePage):

    top_order_button = (By.XPATH, './/div[contains(@class,"Header")]//button[text()="Заказать"]')
    bottom_order_button = (By.XPATH, './/div[contains(@class,"FinishButton")]//button[text()="Заказать"]')
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
    status_button = (By.XPATH, './/button[text()="Посмотреть статус"]')
    scooter_logo = (By.XPATH, './/a[contains(@class,"LogoScooter")]')
    yandex_logo = (By.XPATH, './/a[contains(@class,"LogoYandex")]')

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.find_visible_element(locator).click()
        self.wait_url_to_be(URLs.order_url)

    def fill_input_field(self, input_fild, text):
        self.find_visible_element(input_fild).send_keys(text)

    @allure.step('Заполняем форму заказа')
    def fill_order_form(self, data_set):
        self.fill_input_field(self.name, data_set['name'])
        self.fill_input_field(self.surname, data_set['surname'])
        self.fill_input_field(self.address, data_set['address'])
        self.find_visible_element(self.subway_station_list).click()
        self.find_visible_element(self.subway_station).click()
        self.fill_input_field(self.phone_number, data_set['phone_number'])
        self.find_visible_element(self.next_button).click()
        self.fill_input_field(self.date, data_set['date'])
        self.find_visible_element(self.date).click()
        self.find_visible_element(self.rent_period).click()
        self.find_visible_element(self.period).click()
        self.find_visible_element(self.color).click()
        self.fill_input_field(self.comment, data_set['comment'])
        self.find_visible_element(self.form_order_button).click()
        self.find_visible_element(self.submit_order_button).click()

    def get_order_modal_text(self):
        return self.find_visible_element(self.order_modal).text

    @allure.step('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_popup_success_order(self):
        assert 'Заказ оформлен' in self.get_order_modal_text()

    @allure.step('Проверяем, если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def check_scooter_logo_open_homepage(self):
        self.find_visible_element(self.status_button).click()
        self.find_visible_element(self.scooter_logo).click()
        assert self.current_page() == URLs.base_url

    @allure.step('Проверяем, если нажать на логотип Яндекса, в новом окне откроется главная страница Дзена')
    def check_yandex_logo_open_dzen(self):
        self.find_visible_element(self.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_url_contain('http')
        self.wait_url_not_contain('passport')
        assert URLs.dzen_url in self.current_page(), self.current_page()
