from selenium.webdriver.support.ui import Select
from locators.locators import LocatorsDetailedCalculate, LocatorsBriefCalculate, LocatorsResultCalculate
from pages.base_page import BasePage
from pages.base_page import parse_json


class CalculateCreditPage(BasePage):
    """ Заполнение кредитной формы """

    def enter_data_in_brief_calculate(self, browser):
        """ Заполняем данными блок "Краткий расчёт" """
        field_desired_loan = self.browser.find_element(*LocatorsBriefCalculate.DESIRED_IOAN_LOC)
        field_desired_loan.clear()
        field_desired_loan.send_keys(parse_json("desired_ioan"))

        field_initial_payment = self.browser.find_element(*LocatorsBriefCalculate.INITIAL_PAYMENT_LOC)
        field_initial_payment.clear()
        field_initial_payment.send_keys(parse_json("initial_payment"))

        field_credit_term = self.browser.find_element(*LocatorsBriefCalculate.CREDIT_TERM_LOC)
        field_credit_term.clear()
        field_credit_term.send_keys(parse_json("initial_payment"))

    def enter_data_in_detailed_calculate(self):
        """ Заполняем данными анкету """

        # Заполняем ФИО и паспортные данные
        second_name = self.browser.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC)
        second_name.clear()
        second_name.send_keys(parse_json("second_name"))

        first_name = self.browser.find_element(*LocatorsDetailedCalculate.FIRST_NAME_LOC)
        first_name.clear()
        first_name.send_keys(parse_json("first_name"))

        middle_name = self.browser.find_element(*LocatorsDetailedCalculate.MIDDLE_NAME_LOC)
        middle_name.clear()
        middle_name.send_keys(parse_json("middle_name"))

        passport = self.browser.find_element(*LocatorsDetailedCalculate.PASSPORT_LOC)
        passport.clear()
        passport.send_keys(parse_json("passport"))

        issued_by = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_BY_LOC)
        issued_by.clear()
        issued_by.send_keys(parse_json("issued_by"))

        issued_date = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_DATE_LOC)
        issued_date.clear()
        issued_date.send_keys(parse_json("issued_date"))

        # Выбор данных из выпадающего списка
        education = Select(self.browser.find_element(*LocatorsDetailedCalculate.EDUCATION_LOC))
        education.select_by_visible_text(parse_json("education"))

        seniority = Select(self.browser.find_element(*LocatorsDetailedCalculate.SENIORITY_LOC))
        seniority.select_by_visible_text(parse_json("seniority"))

        term_work_last_place = Select(self.browser.find_element(*LocatorsDetailedCalculate.TERM_WORK_LAST_PLACE_LOC))
        term_work_last_place.select_by_visible_text(parse_json("term_work_last_place"))

        confirmation_income_ndfl = Select(
            self.browser.find_element(*LocatorsDetailedCalculate.CONFIRMATION_INCOME_NDFL_LOC))
        confirmation_income_ndfl.select_by_visible_text(parse_json("confirmation_income_ndfl"))

        work_place_bank_area = Select(self.browser.find_element(*LocatorsDetailedCalculate.WORK_PLACE_BANK_AREA_LOC))
        work_place_bank_area.select_by_visible_text(parse_json("work_place_bank_area"))

        net_income = self.browser.find_element(*LocatorsDetailedCalculate.NET_INCOME_LOC)
        net_income.clear()
        net_income.send_keys(parse_json("net_income"))

        registration_place_bank_area = Select(
            self.browser.find_element(*LocatorsDetailedCalculate.REGISTRATION_PLACE_BANK_AREA_LOC))
        registration_place_bank_area.select_by_visible_text(parse_json("registration_place_bank_area"))

        previous_conviction = Select(self.browser.find_element(*LocatorsDetailedCalculate.PREVIOUS_CONFICTION_LOC))
        previous_conviction.select_by_visible_text(parse_json("previous_conviction"))

        car = Select(self.browser.find_element(*LocatorsDetailedCalculate.CAR_LOC))
        car.select_by_visible_text(parse_json("car"))

        real_estate = Select(self.browser.find_element(*LocatorsDetailedCalculate.REAL_ESTATE_LOC))
        real_estate.select_by_visible_text(parse_json("real_estate"))

    # Проверка результатов расчёта
    def check_message_result_calculate(self):
        field_desired_loan = self.browser.find_element(*LocatorsResultCalculate.CREDIT_MESSAGE_LOC).text
        assert field_desired_loan == parse_json("credit-message"), "Нет сообщения КРЕДИТ ПРЕДВАРИТЕЛЬНО ОДОБРЕН"

    def check_credit_rate(self):
        credit_message = self.browser.find_element(*LocatorsResultCalculate.CREDIT_RATE_LOC).text
        assert credit_message == parse_json("credit-rate"), "Процентная ставка не совпадает"

    def check_credit_monthly_payment_full(self):
        credit_monthly_payment_full = self.browser.find_element(
            *LocatorsResultCalculate.CREDIT_MOTHLY_PAYMENT_FULL_LOC).text
        assert credit_monthly_payment_full == parse_json("credit-monthly-payment-full"), "Ежемесячный платеж не совпадает"

    def check_credit_overpayment(self):
        credit_credit_overpayment = self.browser.find_element(*LocatorsResultCalculate.CREDIT_OVERPAYMENT_LOC).text
        assert credit_credit_overpayment == parse_json("credit-overpayment"), "Переплата по кредиту не совпадает"

    def check_payments_loan_period(self):
        payments_loan_period = self.browser.find_element(*LocatorsResultCalculate.PAYMENTS_IOAN_PERIOD_LOC).text
        assert payments_loan_period == parse_json("payments-loan-period"), "Выплаты за весь срок кредита не совпадают"

    # Методы проверки результатов расчёта в одном месте
    def result_calculate_credit(self):
        self.check_message_result_calculate()  # Проверяем, что есть сообщение "Кредит предварительно одобрен"
        self.check_credit_rate()  # Проверяем, что процентная ставка совпадает с данными тест-кейса
        self.check_credit_monthly_payment_full()  # Проверяем, что ежемесячный платеж совпадает с данными тест-кейса
        self.check_credit_overpayment()  # Проверяем, что переплата по кредиту совпадает с данными тест-кейса
        self.check_payments_loan_period()  # Проверяем, что выплата за весь срок кредита совпадает с тест-кейсом
