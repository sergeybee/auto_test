from .base_page import BasePage
from .locators import LocatorsResultCalculate
from .settings import SettingsDataSet as SD


# Проверяем полученные данные в блоке "Результат расчёта"
class CheckResultCalculateBlock(BasePage):

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

    def check_all_result_calculate_credit(self):
        self.check_message_result_calculate()
        self.check_credit_rate()
        self.check_credit_monthly_payment_full()
        self.check_credit_overpayment()
        self.check_payments_loan_period()



