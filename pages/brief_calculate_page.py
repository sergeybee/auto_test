from .locators import LocatorsBriefCalculate
from .config import SettingsDataSet as SD


# Ввод данных в блок "Краткий расчёт"
class BriefCalculateCredit:

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
