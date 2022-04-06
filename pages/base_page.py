

class BasePage(object):
	"""docstring for BasePage"""
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		#self.browser.implicity_wait(timeout)

	def open(self):
		self.browser.get(self.url)

	def calculate_credit(self):
		self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC).click()