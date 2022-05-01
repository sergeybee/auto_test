from .locators import LocatorsResultCalculate
from .config import SettingsDataSet as SD
from .brief_calculate_page import BriefCalculateCredit
from .detailed_calculate_page import DetailedCalculateCredit


# Проверка полученных данных в блоке "Результат расчёта"
class ResultCalculateCredit():

    def enter_data_in_brief_and_detailed_calculate(self):
        # Заполняем поля Сумма, Взнос и Срок кредита
        bcc = BriefCalculateCredit()
        bcc.enter_data_in_brief_calculate()

        # Заполняем форму детального расчёта
        dcc = DetailedCalculateCredit()
        dcc.enter_data_in_detailed_calculate()

    def check_message_result_calculate(self):
        field_desired_loan = self.browser.find_element(*LocatorsResultCalculate.CREDIT_MESSAGE_LOC).text
        assert field_desired_loan == SD.CREDIT_MESSAGE, "Нет сообщения КРЕДИТ ПРЕДВАРИТЕЛЬНО ОДОБРЕН"

    def check_credit_rate(self):
        credit_message = self.browser.find_element(*LocatorsResultCalculate.CREDIT_RATE_LOC).text
        assert credit_message == SD.CREDIT_RATE, "Процентная ставка не совпадает"

    def check_credit_monthly_payment_full(self):
        credit_monthly_payment_full = self.browser.find_element(*LocatorsResultCalculate.CREDIT_MOTHLY_PAYMENT_FULL_LOC).text
        assert credit_monthly_payment_full == SD.CREDIT_MOTHLY_PAYMENT_FULL, "Ежемесячный платеж не совпадает"

    def check_credit_overpayment(self):
        credit_credit_overpayment = self.browser.find_element(*LocatorsResultCalculate.CREDIT_OVERPAYMENT_LOC).text
        assert credit_credit_overpayment == SD.CREDIT_OVERPAYMENT, "Переплата по кредиту не совпадает"

    def check_payments_loan_period(self):
        payments_loan_period = self.browser.find_element(*LocatorsResultCalculate.PAYMENTS_IOAN_PERIOD_LOC).text
        assert payments_loan_period == SD.PAYMENTS_IOAN_PERIOD, "Выплаты за весь срок кредита не совпадают"

    # Методы проверки результатов расчёта в одном месте
    def check_all_result_calculate_credit(self):
        self.enter_data_in_brief_and_detailed_calculate()    # Заполняем поля калькулятора данными из тест - кейса
        self.check_message_result_calculate()       # Проверяем, что есть сообщение "Кредит предварительно одобрен"
        self.check_credit_rate()                    # Проверяем, что процентная ставка совпадает с данными тест-кейса
        self.check_credit_monthly_payment_full()    # Проверяем, что ежемесячный платеж совпадает с данными тест-кейса
        self.check_credit_overpayment()             # Проверяем, что переплата по кредиту совпадает с данными тест-кейса
        self.check_payments_loan_period()           # Проверяем, что выплата за весь срок кредита совпадает с тест-кейсом



