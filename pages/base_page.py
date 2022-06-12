from .locators import GeneralLocators


class BasePage:
    """docstring for BasePage"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """ Метод открытия страницы сайта """
        self.browser.get(self.url)
        self.browser

    def should_be_site_credit_calculate(self):
        """ Проверяем, что находимся на сайте "Кредитный калькулятор" """
        assert "creditcalculator.pointschool.ru" in self.browser.current_url, "Не тот адрес сайта"

    def should_be_btn_calculate(self):
        """ Проверяем, что есть кнопка "Рассчитать" """
        assert self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC), "Нет кнопки BTN_CALCULATE"

    def btn_calculate_credit_click(self):
        """ Нажимаем на кнопку "Рассчитать" """
        self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC).click()

    def should_be_link_to_question_form(self):
        """ Проверяем, что есть кнопка-ссылка "Заполнить анкету" """
        assert self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC), "Не найдена ссылка или элемент на АНКЕТУ"

    def link_to_question_form_click(self):
        """ Нажимаем на кнопку-ссылку "Заполнить анкету" """
        self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC).click()
