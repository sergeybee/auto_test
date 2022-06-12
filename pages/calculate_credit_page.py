from selenium.webdriver.support.ui import Select
from .locators import LocatorsDetailedCalculate, LocatorsBriefCalculate, LocatorsResultCalculate
import xml.etree.ElementTree as ET


class CalculateCreditPage(object):
    """ Заполнение кредитной формы """
    XML_FILE_PATH = "TestData/DataSet.xml"

    def parse_xml(self):
        """ Парсинг XML документа используя ElementTree """
        try:
            tree = ET.parse(self.XML_FILE_PATH)
            return tree
        except IOError as e:
            print('Ошибка! - не найден файл или директория: %sn' % e)

    def enter_data_in_brief_calculate(self):
        """ Заполняем данными блок "Краткий расчёт" """
        field_desired_loan = self.browser.find_element(*LocatorsBriefCalculate.DESIRED_IOAN_LOC)
        field_desired_loan.clear()
        field_desired_loan.send_keys(self.parse_xml().find('Brief/DESIRED_IOAN').text)

        field_initial_payment = self.browser.find_element(*LocatorsBriefCalculate.INITIAL_PAYMENT_LOC)
        field_initial_payment.clear()
        field_initial_payment.send_keys(self.parse_xml().find('Brief/INITIAL_PAYMENT').text)

        field_credit_term = self.browser.find_element(*LocatorsBriefCalculate.CREDIT_TERM_LOC)
        field_credit_term.clear()
        field_credit_term.send_keys(self.parse_xml().find('Brief/CREDIT_TERM').text)

    def enter_data_in_detailed_calculate(self):
        """ Заполняем данными анкету """

        # Заполняем ФИО и паспортные данные
        second_name = self.browser.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC)
        second_name.clear()
        second_name.send_keys(self.parse_xml().find('Detailed/SECOND_NAME').text)

        first_name = self.browser.find_element(*LocatorsDetailedCalculate.FIRST_NAME_LOC)
        first_name.clear()
        first_name.send_keys(self.parse_xml().find('Detailed/FIRST_NAME').text)

        middle_name = self.browser.find_element(*LocatorsDetailedCalculate.MIDDLE_NAME_LOC)
        middle_name.clear()
        middle_name.send_keys(self.parse_xml().find('Detailed/MIDDLE_NAME').text)

        passport = self.browser.find_element(*LocatorsDetailedCalculate.PASSPORT_LOC)
        passport.clear()
        passport.send_keys(self.parse_xml().find('Detailed/PASSPORT').text)

        issued_by = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_BY_LOC)
        issued_by.clear()
        issued_by.send_keys(self.parse_xml().find('Detailed/ISSUED_BY').text)

        issued_date = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_DATE_LOC)
        issued_date.clear()
        issued_date.send_keys(self.parse_xml().find('Detailed/ISSUED_DATE').text)

        # Выбор данных из выпадающего списка
        education = Select(self.browser.find_element(*LocatorsDetailedCalculate.EDUCATION_LOC))
        education.select_by_visible_text(self.parse_xml().find('Detailed/EDUCATION').text)

        seniority = Select(self.browser.find_element(*LocatorsDetailedCalculate.SENIORITY_LOC))
        seniority.select_by_visible_text(self.parse_xml().find('Detailed/SENIORITY').text)

        term_work_last_place = Select(self.browser.find_element(*LocatorsDetailedCalculate.TERM_WORK_LAST_PLACE_LOC))
        term_work_last_place.select_by_visible_text(self.parse_xml().find('Detailed/TERM_WORK_LAST_PLACE').text)

        confirmation_income_ndfl = Select(
            self.browser.find_element(*LocatorsDetailedCalculate.CONFIRMATION_INCOME_NDFL_LOC))
        confirmation_income_ndfl.select_by_visible_text(self.parse_xml().find('Detailed/CONFIRMATION_INCOME_NDFL').text)

        work_place_bank_area = Select(self.browser.find_element(*LocatorsDetailedCalculate.WORK_PLACE_BANK_AREA_LOC))
        work_place_bank_area.select_by_visible_text(self.parse_xml().find('Detailed/WORK_PLACE_BANK_AREA').text)

        net_income = self.browser.find_element(*LocatorsDetailedCalculate.NET_INCOME_LOC)
        net_income.clear()
        net_income.send_keys(self.parse_xml().find('Detailed/NET_INCOME').text)

        registration_place_bank_area = Select(
            self.browser.find_element(*LocatorsDetailedCalculate.REGISTRATION_PLACE_BANK_AREA_LOC))
        registration_place_bank_area.select_by_visible_text(self.parse_xml().find('Detailed/REGISTRATION_PLACE_BANK_AREA').text)

        previous_conviction = Select(self.browser.find_element(*LocatorsDetailedCalculate.PREVIOUS_CONFICTION_LOC))
        previous_conviction.select_by_visible_text(self.parse_xml().find('Detailed/PREVIOUS_CONFICTION').text)

        car = Select(self.browser.find_element(*LocatorsDetailedCalculate.CAR_LOC))
        car.select_by_visible_text(self.parse_xml().find('Detailed/CAR').text)

        real_estate = Select(self.browser.find_element(*LocatorsDetailedCalculate.REAL_ESTATE_LOC))
        real_estate.select_by_visible_text(self.parse_xml().find('Detailed/REAL_ESTATE').text)

    # Проверка результатов расчёта
    def check_message_result_calculate(self):
        field_desired_loan = self.browser.find_element(*LocatorsResultCalculate.CREDIT_MESSAGE_LOC).text
        assert field_desired_loan == self.parse_xml().find(
            'Result/CREDIT_MESSAGE').text, "Нет сообщения КРЕДИТ ПРЕДВАРИТЕЛЬНО ОДОБРЕН"

    def check_credit_rate(self):
        credit_message = self.browser.find_element(*LocatorsResultCalculate.CREDIT_RATE_LOC).text
        assert credit_message == self.parse_xml().find('Result/CREDIT_RATE').text, "Процентная ставка не совпадает"

    def check_credit_monthly_payment_full(self):
        credit_monthly_payment_full = self.browser.find_element(
            *LocatorsResultCalculate.CREDIT_MOTHLY_PAYMENT_FULL_LOC).text
        assert credit_monthly_payment_full == self.parse_xml().find(
            'Result/CREDIT_MOTHLY_PAYMENT_FULL').text, "Ежемесячный платеж не совпадает"

    def check_credit_overpayment(self):
        credit_credit_overpayment = self.browser.find_element(*LocatorsResultCalculate.CREDIT_OVERPAYMENT_LOC).text
        assert credit_credit_overpayment == self.parse_xml().find(
            'Result/CREDIT_OVERPAYMENT').text, "Переплата по кредиту не совпадает"

    def check_payments_loan_period(self):
        payments_loan_period = self.browser.find_element(*LocatorsResultCalculate.PAYMENTS_IOAN_PERIOD_LOC).text
        assert payments_loan_period == self.parse_xml().find(
            'Result/PAYMENTS_IOAN_PERIOD').text, "Выплаты за весь срок кредита не совпадают"

    # Методы проверки результатов расчёта в одном месте
    def result_calculate_credit(self):
        self.check_message_result_calculate()  # Проверяем, что есть сообщение "Кредит предварительно одобрен"
        self.check_credit_rate()  # Проверяем, что процентная ставка совпадает с данными тест-кейса
        self.check_credit_monthly_payment_full()  # Проверяем, что ежемесячный платеж совпадает с данными тест-кейса
        self.check_credit_overpayment()  # Проверяем, что переплата по кредиту совпадает с данными тест-кейса
        self.check_payments_loan_period()  # Проверяем, что выплата за весь срок кредита совпадает с тест-кейсом
