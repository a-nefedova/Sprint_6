import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Переходим на страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    def current_page(self):
        return self.driver.current_url

    @allure.step('Прокручиваем страницу до элемента')
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_visible_element(locator))

    def find_visible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def click_visible_element(self, locator, time=10):
        self.find_visible_element(locator, time).click()

    def send_keys_to_element(self, locator, text):
        self.find_visible_element(locator).send_keys(text)

    def wait_url_to_be(self, url, time=10):
        WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    def wait_url_not_contain(self, link_part, time=10):
        WebDriverWait(self.driver, time).until(EC.none_of(EC.url_contains(link_part)))

    def wait_url_contain(self, link_part, time=10):
        WebDriverWait(self.driver, time).until(EC.url_contains(link_part))
