from pages.homepage import Homepage
from data import URLs, FAQ
import allure
import pytest


class TestFAQ:

    @allure.title(f'Проверка списка в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('index, question, answer', FAQ.faq_list)
    def test_faq(self, driver, index, question, answer):
        homepage = Homepage(driver)
        homepage.go_to_page(URLs.base_url)
        homepage.scroll_to_element(Homepage.faq)
        actual_question_heading = homepage.find_question(index)
        actual_question_text = actual_question_heading.text
        actual_question_heading.click()
        actual_answer_text = homepage.get_answer_text(index)
        assert (actual_question_text == question) and (actual_answer_text == answer)
