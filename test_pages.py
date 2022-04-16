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
        base_page.all_methods()
        time.sleep(1)

    # Тест "КРАТКОГО РАСЧЁТА"
    def test_brief_calculate(self):
        brief_page = BriefCalculateCredit(browser, browser.current_url)
        brief_page.enter_data_in_brief_calculate()
        self.btn_calculate_credit_click()

    # Тест "ПОДРОБНОГО РАСЧЁТА":
    def test_detailed_calculate(self):
        detailed_page = DetailedCalculateCredit(browser, browser.current_url)
        self.test_brief_calculate()
        detailed_page.enter_data_in_detailed_calculate()
        self.btn_calculate_credit_click()

    # Тест "РЕЗУЛЬТАТА РАСЧЁТА"
    def test_result_calculate(self):
        result = ResultCalculateCredit(browser, browser.current_url)
        result.check_all_result_calculate_credit()
