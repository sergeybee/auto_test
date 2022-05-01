from .locators import GeneralLocators


class BasePage:
    """docstring for BasePage"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Метод открытия страницы сайта
    def open(self):
        self.browser.get(self.url)

    # Проверяем, что находимся на сайте "Кредитный калькулятор"
    def should_be_site_credit_calculate(self):
        assert "creditcalculator.pointschool.ru" in self.browser.current_url, "Не тот адрес сайта"

    # Проверяем, что есть кнопка "Рассчитать"
    def should_be_btn_calculate(self):
        assert self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC), "Нет кнопки BTN_CALCULATE"

    # Нажимаем на кнопку "Рассчитать"
    def btn_calculate_credit_click(self):
        self.browser.find_element(*GeneralLocators.BTN_CALCULATE_LOC).click()

    # Проверяем, что есть кнопка-ссылка "Заполнить анкету"
    def should_be_link_to_question_form(self):
        assert self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC), "Не найдена ссылка или элемент на АНКЕТУ"

    # Нажимаем на кнопку-ссылку "Заполнить анкету"
    def link_to_question_form_click(self):
        self.browser.find_element(*GeneralLocators.LINK_ANKET_LOC).click()
