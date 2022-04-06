from .base_page import BasePage
from .settings import *
from .locators import GeneralLocators
from selenium.webdriver.common.by import By


# TODO: Добавить проверки на пустые поля в кратком расчете
# В этом классе осуществляем проверку, что находимся именно на сайте Кредитного калькулятора
# и что на нем присутствует кнопка Рассчитать, после чего кликаем на нее

class MainPage(BasePage):

#Проверяем, что находимся на сайте creditcalculator.pointschool.ru
	def should_be_point_url(self):
		assert "pointschool" in self.browser.current_url, "This is not a url"

# Проверяем, что есть кнопка "Рассчитать"
	def should_be_btn_calculate(self):
		assert self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC), "This is not BTN_CALCULATE element"

# Проверяем, что есть ссылка ЗАПОЛНИТЬ АНКЕТУ
	def should_be_link_to_question_form(self):
		assert self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC)

class CheckingTestDataSet:
	def check_test_dataset_brief_calculate():
		second_name = self.browser.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC).text
		field_initial_payment = self.browser.find_element(*LocatorsBriefCalculate.FIELD_INITIAL_PAYMENT_LOC).text
		field_credit_term = self.browser.find_element(*LocatorsBriefCalculate.FIELD_CREDIT_TERM_LOC).text
		assert second_name == FIELD_DESIRED_IOAN and field_initial_payment == FIELD_INITIAL_PAYMENT and field_credit_term == FIELD_CREDIT_TERM, "Error DataSet in Brief Block"

	def check_test_dataset_detailed_calculate():
		second_name = self.browser.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC).text
		assert second_name == FIELD_DESIRED_IOAN