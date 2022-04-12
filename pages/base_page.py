from .locators import GeneralLocators

class BasePage(object):
	"""docstring for BasePage"""
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)

	def btn_calculate_credit_click(self):
		self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC).click()

	def link_to_question_form_click(self):
		self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC).click()


class MainPage(BasePage):
	# Проверяем, что находимся на сайте creditcalculator.pointschool.ru
	def should_be_site_credit_calculate(self):
		assert "creditcalculator.pointschool.ru" in self.browser.current_url, "This is not a url"

	# Проверяем, что есть кнопка "Рассчитать"
	def should_be_btn_calculate(self):
		assert self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC), "This is not BTN_CALCULATE element"

	# Проверяем, что есть ссылка ЗАПОЛНИТЬ АНКЕТУ
	def should_be_link_to_question_form(self):
		assert self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC), "Не найдена ссылка или элемент на АНКЕТУ"
