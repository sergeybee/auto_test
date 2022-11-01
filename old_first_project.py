# Авто тест кредитного калькулятора на сайте http://creditcalculator.pointschool.ru/
# по тест кейсу https://docs.google.com/document/d/1ILdnEONI576Olapt5jUbUcfUe0i_DmFR/edit
# Из курса ПОИНТ
# Версия 1.0
# Развитие версий: Версия 1.0, Версия 1.1
# Статус: Переписан полностью. Это моя первая работа :))))))))

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

URL = 'http://creditcalculator.pointschool.ru/credit#'

try:
    driver.get(URL)

    btn_result = driver.find_element(By.CSS_SELECTOR, "button[data-btn-action='do-result']").click()
    driver.find_element(*JointLocators.BTN_CALCULATE).click()

    link_anket = driver.find_element(By.XPATH, "//a[contains(text(),'заполните анкету')]").click()
    driver.find_element(*JointLocators.LINK_ANKET).click()


# Заполняем Сумма, Первоначальный взнос, Срок кредита
    field_desired_loan = driver.find_element(By.CSS_SELECTOR, "input[name='field-desired-loan']")
    field_desired_loan.clear()
    field_desired_loan.send_keys("100000")

    field_initial_payment = driver.find_element(By.CSS_SELECTOR, "input[name='field-initial-payment']")
    field_initial_payment.clear()
    field_initial_payment.send_keys("0")

    field_credit_term = driver.find_element(By.CSS_SELECTOR, "input[name='field-credit-term']")
    field_credit_term.clear()
    field_credit_term.send_keys("12")

# Заполняем ФИО и паспортные данные клиента
    second_name = driver.find_element(By.CSS_SELECTOR, "input[name='second-name']")
    second_name.clear()
    second_name.send_keys("Ярцова")

    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.clear()
    first_name.send_keys("Злата")

    middle_name = driver.find_element(By.CSS_SELECTOR, "input[name='middle-name']")
    middle_name.clear()
    middle_name.send_keys("Васильевна")

    passport = driver.find_element(By.CSS_SELECTOR, "input[name='passport']")
    passport.clear()
    passport.send_keys("4300 542277")

    issued_by = driver.find_element(By.CSS_SELECTOR, "input[name='issued-by']")
    issued_by.clear()
    issued_by.send_keys("Нижегородское ГОВД")

    issued_date = driver.find_element(By.CSS_SELECTOR, "input[name='issued-date']")
    issued_date.clear()
    issued_date.send_keys("11.11.2011")

    # Выбор данных из выпадающего списка

    education = Select(driver.find_element(By.NAME, "education"))                                        # Образование
    education.select_by_visible_text("Высшее")

    seniority = Select(driver.find_element(By.NAME, "seniority"))                                        # Общий трудовой стаж
    seniority.select_by_visible_text("5 лет - 10 лет")

    term_work_last_place = Select(driver.find_element(By.NAME, "term-work-last-place"))                  # Срок работы на последнем месте
    term_work_last_place.select_by_visible_text("Более 3 лет")

    confirmation_income_ndfl = Select(driver.find_element(By.NAME, "confirmation-income-ndfl"))          # Подтверждение дохода справкой 2НДФЛ
    confirmation_income_ndfl.select_by_visible_text("Да")

    work_place_bank_area = Select(driver.find_element(By.NAME, "work-place-bank-area"))                  # Место работы в регионе регистрации банка?
    work_place_bank_area.select_by_visible_text("Да")

    net_income = driver.find_element(By.CSS_SELECTOR, "input[name='net-income']")                        # Чистый доход в месяц
    net_income.clear()
    net_income.send_keys("35000")

    registration_place_bank_area = Select(driver.find_element(By.NAME, "registration-place-bank-area"))  # Место прописки в регионе регистрации банка?
    registration_place_bank_area.select_by_visible_text("Да")

    previous_conviction = Select(driver.find_element(By.NAME, "previous-conviction"))                    # Есть ли у вас судимость?
    previous_conviction.select_by_visible_text("Нет")

    car = Select(driver.find_element(By.NAME, "car"))                                                    # Есть ли у вас в собственности автомобиль?
    car.select_by_visible_text("Да")

    real_estate = Select(driver.find_element(By.NAME, "real-estate"))                                    # Есть ли у вас в собственности недвижимость?
    real_estate.select_by_visible_text("Да")

    driver.find_element(*JointLocators.BTN_CALCULATE).click()

    time.sleep(10)

# Проверка результатов расчета

    assert "Кредит предварительно одобрен" in driver.find_element(By.CSS_SELECTOR, 'div[id="credit-message"]').text

    credit_message = driver.find_element(By.CSS_SELECTOR, 'div[id="credit-message"]').text
    credit_rate = driver.find_element(By.ID, "credit-rate").text
    credit_monthly_payment_full = driver.find_element(By.ID, "credit-monthly-payment-full").text
    credit_credit_overpayment = driver.find_element(By.ID, "credit-credit-overpayment").text
    payments_loan_period = driver.find_element(By.ID, "payments-loan-period").text

# Проверяем что имеем значения расчётов принтом
    print(credit_message)

except Exception as ex:
    print(ex)
