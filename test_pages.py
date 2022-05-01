import pytest
from .pages.brief_calculate_page import BriefCalculateCredit
from .pages.detailed_calculate_page import DetailedCalculateCredit
from .pages.result_calculate_page import ResultCalculateCredit
from .pages.base_page import BasePage
import time


class TestCalculateCreditBase(BasePage):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://creditcalculator.pointschool.ru"
        base_page = BasePage(browser, link)
        base_page.open()
        # Перед каждым запуском теста проводим проверку на наличие элементов на сайте
        base_page.should_be_site_credit_calculate()     # Проверяем, что находимся на сайте "Кредитный калькулятор"
        base_page.should_be_btn_calculate()             # Проверяем, что есть кнопка "Рассчитать"
        base_page.btn_calculate_credit_click()          # Нажимаем на кнопку "Рассчитать"
        base_page.should_be_link_to_question_form()     # Проверяем, что есть кнопка-ссылка "Заполнить анкету"
        base_page.link_to_question_form_click()         # Нажимаем на кнопку-ссылку "Заполнить анкету"
        time.sleep(1)

    # Тест "КРАТКОГО РАСЧЁТА"
    # @pytest.mark.brief_calc
    def test_brief_calculate(self):
        bcc = BriefCalculateCredit()
        bcc.enter_data_in_brief_calculate()
        self.btn_calculate_credit_click()

    # Тест "ПОДРОБНОГО РАСЧЁТА":
    # @pytest.mark.detailed_calc
    def test_detailed_calculate(self):
        dcc = DetailedCalculateCredit()
        dcc.enter_data_in_detailed_calculate()
        self.btn_calculate_credit_click()

    # Тест "РЕЗУЛЬТАТОВ РАСЧЁТА"
    # @pytest.mark.result_calc
    def test_result_calculate(self):
        result = ResultCalculateCredit()
        result.check_all_result_calculate_credit()
