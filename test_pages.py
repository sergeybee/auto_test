import pytest

from pages.brief_calculate_page import EnteringDataBriefCalculateBlock
from pages.detailed_calculate_page import DetailedCalculateCredit
from pages.result_calculate_page import CheckResultCalculateBlock
from pages.base_page import MainPage
import time


# Тест наличия элементов на сайте
class TestBasePage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        """
        setup-функция, подготавливает данные и выполняется перед запуском каждого теста из класса
        Открывает форму регистрации, регистрирует нового пользователя
        Проверяет, что пользователь залогинен
        """
        link = "http://creditcalculator.pointschool.ru"
        page = MainPage(browser, link)
        page.open()
        page.should_be_site_credit_calculate()
        page.should_be_btn_calculate()
        page.btn_calculate_credit_click()
        time.sleep(2)
        page.should_be_link_to_question_form()
        page.link_to_question_form_click()
        time.sleep(2)

    # Тест "КРАТКОГО РАСЧЁТА"
    @pytest.mark.brief_calc
    def test_guest_can_enter_data_in_brief_calculate_block(self, browser):
        brief_page = EnteringDataBriefCalculateBlock(browser, browser.current_url)
        brief_page.entering_data_in_brief_calculate()
        time.sleep(2)

    # Тест "ПОДРОБНОГО РАСЧЁТА"
    @pytest.mark.detailed_calc
    def test_guest_entering_data_in_detailed_calculate(self, browser):
        brief_page = EnteringDataBriefCalculateBlock(browser, browser.current_url)
        brief_page.entering_data_in_brief_calculate()

        detailed_page = DetailedCalculateCredit(browser, browser.current_url)
        detailed_page.entering_data_in_detailed_calculate()
        detailed_page.btn_calculate_credit_click()
        time.sleep(3)

    # Тест "РЕЗУЛЬТАТА РАСЧЁТА"
    @pytest.mark.result_calc
    def test_result_calculate(self, browser):
        brief_page = EnteringDataBriefCalculateBlock(browser, browser.current_url)
        brief_page.entering_data_in_brief_calculate()

        detailed_page = DetailedCalculateCredit(browser, browser.current_url)
        detailed_page.entering_data_in_detailed_calculate()
        detailed_page.btn_calculate_credit_click()
        time.sleep(3)

        result = CheckResultCalculateBlock(browser, browser.current_url)
        result.check_all_result_calculate_credit()
        time.sleep(3)
