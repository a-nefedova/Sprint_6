from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class Homepage(BasePage):

    faq = (By.XPATH, './/div[text()="Вопросы о важном"]')

    @allure.step('Находим вопрос по индексу')
    def find_question(self, index):
        return self.find_visible_element((By.ID, f'accordion__heading-{index}'))

    @allure.step('Находим ответ по индексу')
    def get_answer_text(self, index):
        return self.find_visible_element((By.ID, f'accordion__panel-{index}')).text
