from base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators import LocatorsBriefCalculate
from settings import SettingsDataSet

# Вводим данные в блок КРАТКОГО РАСЧЕТА
class BriefCalculateCredit(BasePage):

	def entering_data_in_brief_calculate():
	    field_desired_loan = driver.find_element(*LocatorsBriefCalculate.FIELD_DESIRED_IOAN_LOC)
	    field_desired_loan.clear()
	    field_desired_loan.send_keys(FIELD_DESIRED_IOAN)

	    field_initial_payment = driver.find_element(*LocatorsBriefCalculate.FIELD_INITIAL_PAYMENT_LOC)
	    field_initial_payment.clear()
	    field_initial_payment.send_keys(FIELD_INITIAL_PAYMENT)

	    field_credit_term = driver.find_element(*LocatorsBriefCalculate.FIELD_CREDIT_TERM_LOC)
	    field_credit_term.clear()
	    field_credit_term.send_keys(FIELD_CREDIT_TERM)