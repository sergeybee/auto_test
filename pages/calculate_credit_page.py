from selenium.webdriver.support.ui import Select
from .locators import LocatorsDetailedCalculate
from .config import SettingsDataSet as SD
from .brief_calculate_page import BriefCalculateCredit
from .base_page import BasePage


class BriefCalculateCredit():
    # Заполняем поля Сумма, Взнос и Срок кредита
    def enter_data_in_brief_calculate(self):
        field_desired_loan = self.browser.find_element(*LocatorsBriefCalculate.FIELD_DESIRED_IOAN_LOC)
        field_desired_loan.clear()
        field_desired_loan.send_keys(SD.FIELD_DESIRED_IOAN)

        field_initial_payment = self.browser.find_element(*LocatorsBriefCalculate.FIELD_INITIAL_PAYMENT_LOC)
        field_initial_payment.clear()
        field_initial_payment.send_keys(SD.FIELD_INITIAL_PAYMENT)

        field_credit_term = self.browser.find_element(*LocatorsBriefCalculate.FIELD_CREDIT_TERM_LOC)
        field_credit_term.clear()
        field_credit_term.send_keys(SD.FIELD_CREDIT_TERM)


class DetailedCalculateCredit():

    # Заполняем поля анкеты подробного расчёта
    def enter_data_in_detailed_calculate(self):
        # # Заполняем поля Сумма, Взнос и Срок кредита
        # BriefCalculateCredit.enter_data_in_brief_calculate(self.browser)

        # Заполняем ФИО и паспортные данные
        second_name = self.browser.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC)
        second_name.clear()
        second_name.send_keys(SD.SECOND_NAME)

        first_name = self.browser.find_element(*LocatorsDetailedCalculate.FIRST_NAME_LOC)
        first_name.clear()
        first_name.send_keys(SD.FIRST_NAME)

        middle_name = self.browser.find_element(*LocatorsDetailedCalculate.MIDDLE_NAME_LOC)
        middle_name.clear()
        middle_name.send_keys(SD.MIDDLE_NAME)

        passport = self.browser.find_element(*LocatorsDetailedCalculate.PASSPORT_LOC)
        passport.clear()
        passport.send_keys(SD.PASSPORT)

        issued_by = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_BY_LOC)
        issued_by.clear()
        issued_by.send_keys(SD.ISSUED_BY)

        issued_date = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_DATE_LOC)
        issued_date.clear()
        issued_date.send_keys(SD.ISSUED_DATE)

        # Выбор данных из выпадающего списка
        education = Select(self.browser.find_element(*LocatorsDetailedCalculate.EDUCATION_LOC))
        education.select_by_visible_text(SD.EDUCATION)

        seniority = Select(self.browser.find_element(*LocatorsDetailedCalculate.SENIORITY_LOC))
        seniority.select_by_visible_text(SD.SENIORITY)

        term_work_last_place = Select(self.browser.find_element(*LocatorsDetailedCalculate.TERM_WORK_LAST_PLACE_LOC))
        term_work_last_place.select_by_visible_text(SD.TERM_WORK_LAST_PLACE)

        confirmation_income_ndfl = Select(self.browser.find_element(*LocatorsDetailedCalculate.CONFIRMATION_INCOME_NDFL_LOC))
        confirmation_income_ndfl.select_by_visible_text(SD.CONFIRMATION_INCOME_NDFL)

        work_place_bank_area = Select(self.browser.find_element(*LocatorsDetailedCalculate.WORK_PLACE_BANK_AREA_LOC))
        work_place_bank_area.select_by_visible_text(SD.WORK_PLACE_BANK_AREA)

        net_income = self.browser.find_element(*LocatorsDetailedCalculate.NET_INCOME_LOC)
        net_income.clear()
        net_income.send_keys(SD.NET_INCOME)

        registration_place_bank_area = Select(self.browser.find_element(*LocatorsDetailedCalculate.REGISTRATION_PLACE_BANK_AREA_LOC))
        registration_place_bank_area.select_by_visible_text(SD.REGISTRATION_PLACE_BANK_AREA)

        previous_conviction = Select(self.browser.find_element(*LocatorsDetailedCalculate.PREVIOUS_CONFICTION_LOC))
        previous_conviction.select_by_visible_text(SD.PREVIOUS_CONFICTION)

        car = Select(self.browser.find_element(*LocatorsDetailedCalculate.CAR_LOC))
        car.select_by_visible_text(SD.CAR)

        real_estate = Select(self.browser.find_element(*LocatorsDetailedCalculate.REAL_ESTATE_LOC))
        real_estate.select_by_visible_text(SD.REAL_ESTATE)


class ResultCalculateCredit():

    def check_message_result_calculate(self):
        field_desired_loan = self.browser.find_element(*LocatorsResultCalculate.CREDIT_MESSAGE_LOC).text
        assert field_desired_loan == SD.CREDIT_MESSAGE, "Нет сообщения КРЕДИТ ПРЕДВАРИТЕЛЬНО ОДОБРЕН"

    def check_credit_rate(self):
        credit_message = self.browser.find_element(*LocatorsResultCalculate.CREDIT_RATE_LOC).text
        assert credit_message == SD.CREDIT_RATE, "Процентная ставка не совпадает"

    def check_credit_monthly_payment_full(self):
        credit_monthly_payment_full = self.browser.find_element(
            *LocatorsResultCalculate.CREDIT_MOTHLY_PAYMENT_FULL_LOC).text
        assert credit_monthly_payment_full == SD.CREDIT_MOTHLY_PAYMENT_FULL, "Ежемесячный платеж не совпадает"

    def check_credit_overpayment(self):
        credit_credit_overpayment = self.browser.find_element(*LocatorsResultCalculate.CREDIT_OVERPAYMENT_LOC).text
        assert credit_credit_overpayment == SD.CREDIT_OVERPAYMENT, "Переплата по кредиту не совпадает"

    def check_payments_loan_period(self):
        payments_loan_period = self.browser.find_element(*LocatorsResultCalculate.PAYMENTS_IOAN_PERIOD_LOC).text
        assert payments_loan_period == SD.PAYMENTS_IOAN_PERIOD, "Выплаты за весь срок кредита не совпадают"

    # Методы проверки результатов расчёта в одном месте
    def check_all_result_calculate_credit(self):
        self.enter_data_in_brief_and_detailed_calculate()  # Заполняем поля калькулятора данными из тест - кейса
        self.check_message_result_calculate()  # Проверяем, что есть сообщение "Кредит предварительно одобрен"
        self.check_credit_rate()  # Проверяем, что процентная ставка совпадает с данными тест-кейса
        self.check_credit_monthly_payment_full()  # Проверяем, что ежемесячный платеж совпадает с данными тест-кейса
        self.check_credit_overpayment()  # Проверяем, что переплата по кредиту совпадает с данными тест-кейса
        self.check_payments_loan_period()  # Проверяем, что выплата за весь срок кредита совпадает с тест-кейсом
