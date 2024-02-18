import allure
from utils.urls import Urls
from pages.home_page import YaScooterHomePage


@allure.epic('Эпик_Upgrade Main page / ui usability')
@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_Header')
class TestYaScooterHomePage:

    @allure.feature('Фича_Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Стори_Переход к "Оформление заказа" по кнопке "Заказать" из header')
    @allure.title('Нажатия на кнопку "Заказать" в header.')
    @allure.description('Проверка что, на домашней странице в header по кнопке "Заказать", '
                        'просходит корректный переход на страницу "Оформления заказа".')
    def test_click_top_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_top_order_button()
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Фича_Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Стори_Переход к "Оформление заказа" по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Нажатие на кнопку "Заказать", в блоке "Как это работает".')
    @allure.description('Проверка что, на домашней странице в блоке "Как это работает" по кнопке "Заказать", '
                        'просходит корректный переход на страницу "Оформления заказа".')
    def test_click_bottom_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Фича_Переход на страницу "ЯндексДзен" из Домашней страницы')
    @allure.story("Стори_Редирект на страницу ЯндексДзен по кнопке logo в header")
    @allure.title('При нажатии на лого "ЯндексСамокат" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка что, на домашней странице в header по кнопке "ЯндексСамокат" '
                        'происходит корреткный редирект на страницу "ЯндексДзен".')
    def test_click_yandex_button_go_to_yandex(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_yandex_button()
        ya_scooter_home_page.switch_window(1)
        ya_scooter_home_page.wait_url_until_not_about_blank()
        current_url = ya_scooter_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url)
