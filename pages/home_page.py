import allure
from pages.base_page import BasePage
from utils.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import YaScooterHomePageLocator as Locators
from selenium.webdriver.support import expected_conditions as EC


class YaScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        return elems[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.YANDEX_SITE_BUTTON).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.COOKIE_ACCEPT_BUTTON).click()
