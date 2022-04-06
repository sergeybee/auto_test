
# Авто тест кредитного калькулятора на сайте http://creditcalculator.pointschool.ru/
# по тест кейсу https://docs.google.com/document/d/1ILdnEONI576Olapt5jUbUcfUe0i_DmFR/edit
# Из курса ПОИНТ
# Развитие версий: Версия 1.0, Версия 1.1
# Статус: В РАБОТЕ ЕЩЕ

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from locators import *

URL = 'http://creditcalculator.pointschool.ru/credit#'

driver = webdriver.Chrome()

try:
    driver.get(URL)

    driver.find_element(*JointLocators.BTN_CALCULATE).click()

    driver.find_element(*JointLocators.LINK_ANKET).click()


# Заполняем Сумма, Первоначальный взнос, Срок кредита
    field_desired_loan = driver.find_element(*LocatorsBriefCalculate.FIELD_DESIRED_IOAN)
    field_desired_loan.clear()
    field_desired_loan.send_keys("100000")

    field_initial_payment = driver.find_element(*LocatorsBriefCalculate.FIELD_INITIAL_PAYMENT)
    field_initial_payment.clear()
    field_initial_payment.send_keys("0")

    field_credit_term = driver.find_element(*LocatorsBriefCalculate.FIELD_CREDIT_TERM)
    field_credit_term.clear()
    field_credit_term.send_keys("12")

# Заполняем ФИО и паспортные данные клиента
    second_name = driver.find_element(*LocatorsDetailedCalculate.SECOND_NAME)
    second_name.clear()
    second_name.send_keys("Ярцова")
    
    first_name = driver.find_element(*LocatorsDetailedCalculate.FIRST_NAME)
    first_name.clear()
    first_name.send_keys("Злата")

    middle_name = driver.find_element(*LocatorsDetailedCalculate.MIDDLE_NAME)
    middle_name.clear()
    middle_name.send_keys("Васильевна")

    passport = driver.find_element(*LocatorsDetailedCalculate.PASSPORT)
    passport.clear()
    passport.send_keys("4300 542277")

    issued_by = driver.find_element(*LocatorsDetailedCalculate.ISSUED_BY)
    issued_by.clear()
    issued_by.send_keys("Нижегородское ГОВД")
    
    issued_date = driver.find_element(*LocatorsDetailedCalculate.ISSUED_DATE)
    issued_date.clear()
    issued_date.send_keys("11.11.2011")

    # Выбор данных из выпадающего списка

    education = Select(driver.find_element(*LocatorsDetailedCalculate.EDUCATION))                                        # Образование
    education.select_by_visible_text("Высшее")
    
    seniority = Select(driver.find_element(*LocatorsDetailedCalculate.SENIORITY))                                        # Общий трудовой стаж
    seniority.select_by_visible_text("5 лет - 10 лет")

    term_work_last_place = Select(driver.find_element(*LocatorsDetailedCalculate.TERM_WORK_LAST_PLACE))                  # Срок работы на последнем месте
    term_work_last_place.select_by_visible_text("Более 3 лет")

    confirmation_income_ndfl = Select(driver.find_element(*LocatorsDetailedCalculate.CONFIRMATION_INCOME_NDFL))          # Подтверждение дохода справкой 2НДФЛ
    confirmation_income_ndfl.select_by_visible_text("Да")

    work_place_bank_area = Select(driver.find_element(*LocatorsDetailedCalculate.WORK_PLACE_BANK_AREA))                  # Место работы в регионе регистрации банка?
    work_place_bank_area.select_by_visible_text("Да")

    net_income = driver.find_element(*LocatorsDetailedCalculate.NET_INCOME)                        # Чистый доход в месяц
    net_income.clear()
    net_income.send_keys("35000")

    registration_place_bank_area = Select(driver.find_element(*LocatorsDetailedCalculate.REGISTRATION_PLACE_BANK_AREA))  # Место прописки в регионе регистрации банка?
    registration_place_bank_area.select_by_visible_text("Да")

    previous_conviction = Select(driver.find_element(*LocatorsDetailedCalculate.PREVIOUS_CONFICTION))                    # Есть ли у вас судимость?
    previous_conviction.select_by_visible_text("Нет")

    car = Select(driver.find_element(*LocatorsDetailedCalculate.CAR))                                                    # Есть ли у вас в собственности автомобиль?
    car.select_by_visible_text("Да")

    real_estate = Select(driver.find_element(*LocatorsDetailedCalculate.REAL_ESTATE))                                    # Есть ли у вас в собственности недвижимость?
    real_estate.select_by_visible_text("Да")

    driver.find_element(*JointLocators.BTN_CALCULATE).click()

    time.sleep(10)

# Проверка результатов расчета

    assert "Кредит предварительно одобрен" in driver.find_element(By.CSS_SELECTOR, 'div[id="credit-message"]').text
    
    credit_message = driver.find_element(*LocatorsResultCalcBlock.CREDIT_MESSAGE).text
    credit_rate = driver.find_element(*LocatorsResultCalcBlock.CREDIT_RATE).text
    credit_monthly_payment_full = driver.find_element(*LocatorsResultCalcBlock.CREDIT_MOTHLY_PAYMENT_FULL).text
    credit_credit_overpayment = driver.find_element(*LocatorsResultCalcBlock.CREDIT_OVERPAYMENT).text
    payments_loan_period = driver.find_element(*LocatorsResultCalcBlock.PAYMENTS_IOAN_PERIOD).text

# Проверяем что имеем значения расчётов принтом    
    print(credit_message)
    print(credit_rate)
    print(credit_monthly_payment_full)
    print(credit_credit_overpayment)
    print(payments_loan_period)

    time.sleep(10)

###################   Эту часть не доделал ###################

#     if print("Кредит предаварительно одобрен")
    
#     if credit_rate == "28.61 %":
#         print("Процентная ставка 28.61 %")
#     else: 
#         print("ОШИБКА: Процентная ставка не совпадает с расчетом")

#     if credit_monthly_payment_full == "9 680 Р":
#         print("Ежемесячный платеж 9 680 Р")
#     else: 
#         print("ОШИБКА: Ежемесячный платеж не совпадает с расчетом")     

#     if credit_credit_overpayment == "16 165 Р":
#         print("Переплата по кредиту 16 165 Р")
#     else: 
#         print("ОШИБКА: Переплата по кредиту не совпадает с расчетом")   

#     if credit_credit_overpayment == "116 165 Р":
#         print("Выплаты за весь срок кредита 116 165 Р")
#     else: 
#         print("ОШИБКА: Выплаты за весь срок кредита не совпадает с расчетом")
    
except Exception as ex:
    print(ex)
    
finally:
    driver.quit()