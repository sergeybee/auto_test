from pages.base_page import BasePage
from pages.calculate_credit_page import CalculateCreditPage
import time
import pytest
from config import MAIN_LINK


class TestCalculateCreditBase(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        base_page = BasePage(browser, MAIN_LINK)
        base_page.open()
        # Перед каждым запуском теста проводим проверку на наличие элементов на сайте
        base_page.should_be_site_credit_calculate()     # Проверяем, что находимся на сайте "Кредитный калькулятор"
        base_page.should_be_btn_calculate()             # Проверяем, что есть кнопка "Рассчитать"
        base_page.btn_calculate_credit_click()          # Нажимаем на кнопку "Рассчитать"
        base_page.should_be_link_to_question_form()     # Проверяем, что есть кнопка-ссылка "Заполнить анкету"
        base_page.link_to_question_form_click()         # Нажимаем на кнопку-ссылку "Заполнить анкету"
        time.sleep(1)

    def test_calculate_credit(self, browser):
        """ Тест "КРАТКОГО РАСЧЁТА """
        link = "http://creditcalculator.pointschool.ru"
        bcc = CalculateCreditPage(browser, link)
        bcc.enter_data_in_brief_calculate()
        bcc.enter_data_in_detailed_calculate()
        bcc.btn_calculate_credit_click()
        time.sleep(5)
        bcc.result_calculate_credit()
