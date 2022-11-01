from selenium.webdriver.common.by import By


class GeneralLocators:
    """ Общие локаторы кнопок для модулей краткого и подробного расчёта	"""
    BTN_CALCULATE_LOC = (By.CSS_SELECTOR, "button[data-btn-action='do-result']")
    LINK_ANKET_LOC = (By.XPATH, "//a[contains(text(),'заполните анкету')]")


class LocatorsBriefCalculate:
    """Локаторы примерного модуля (блока) расчета"""

    DESIRED_IOAN_LOC = (By.CSS_SELECTOR, "input[name='field-desired-loan']")
    INITIAL_PAYMENT_LOC = (By.CSS_SELECTOR, "input[name='field-initial-payment']")
    CREDIT_TERM_LOC = (By.CSS_SELECTOR, "input[name='field-credit-term']")


class LocatorsDetailedCalculate:
    """Локаторы подробного модуля (блока) расчета"""

    SECOND_NAME_LOC = (By.CSS_SELECTOR, "input[name='second-name']")
    FIRST_NAME_LOC = (By.CSS_SELECTOR, "input[name='first-name']")
    MIDDLE_NAME_LOC = (By.CSS_SELECTOR, "input[name='middle-name']")
    PASSPORT_LOC = (By.CSS_SELECTOR, "input[name='passport']")
    ISSUED_BY_LOC = (By.CSS_SELECTOR, "input[name='issued-by']")
    ISSUED_DATE_LOC = (By.CSS_SELECTOR, "input[name='issued-date']")
    EDUCATION_LOC = (By.NAME, "education")
    SENIORITY_LOC = (By.NAME, "seniority")
    TERM_WORK_LAST_PLACE_LOC = (By.NAME, "term-work-last-place")
    CONFIRMATION_INCOME_NDFL_LOC = (By.NAME, "confirmation-income-ndfl")
    WORK_PLACE_BANK_AREA_LOC = (By.NAME, "work-place-bank-area")
    NET_INCOME_LOC = (By.CSS_SELECTOR, "input[name='net-income']")
    REGISTRATION_PLACE_BANK_AREA_LOC = (By.NAME, "registration-place-bank-area")
    PREVIOUS_CONFICTION_LOC = (By.NAME, "previous-conviction")
    CAR_LOC = (By.NAME, "car")
    REAL_ESTATE_LOC = (By.NAME, "real-estate")


class LocatorsResultCalculate:
    """Локаторы блока с результатами расчета"""
    CREDIT_MESSAGE_LOC = (By.CSS_SELECTOR, "div[id='credit-message']")
    CREDIT_RATE_LOC = (By.ID, "credit-rate")
    CREDIT_MOTHLY_PAYMENT_FULL_LOC = (By.ID, "credit-monthly-payment-full")
    CREDIT_OVERPAYMENT_LOC = (By.ID, "credit-credit-overpayment")
    PAYMENTS_IOAN_PERIOD_LOC = (By.ID, "payments-loan-period")
