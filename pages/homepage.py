from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class Homepage(BasePage):

    top_order_button = (By.XPATH, './/div[contains(@class,"Header")]//button[text()="Заказать"]')
    bottom_order_button = (By.XPATH, './/div[contains(@class,"FinishButton")]//button[text()="Заказать"]')
    scooter_logo = (By.XPATH, './/a[contains(@class,"LogoScooter")]')
    yandex_logo = (By.XPATH, './/a[contains(@class,"LogoYandex")]')
    faq = (By.XPATH, './/div[text()="Вопросы о важном"]')

    @allure.step('Находим вопрос по индексу')
    def find_question(self, index):
        return self.find_visible_element((By.ID, f'accordion__heading-{index}'))

    @allure.step('Находим ответ по индексу')
    def get_answer_text(self, index):
        return self.find_visible_element((By.ID, f'accordion__panel-{index}')).text
