from base_page import BasePage
from locators import LocatorsResultCalculate


# Блок с результатами расчёта
class ResultCalculateCredit(BasePage):

    assert "Кредит предварительно одобрен" in driver.find_element(By.CSS_SELECTOR, 'div[id="credit-message"]').text
    
    credit_message = driver.find_element(*LocatorsResultCalculate.CREDIT_MESSAGE).text
    credit_rate = driver.find_element(*LocatorsResultCalculate.CREDIT_RATE).text
    credit_monthly_payment_full = driver.find_element(*LocatorsResultCalculate.CREDIT_MOTHLY_PAYMENT_FULL).text
    credit_credit_overpayment = driver.find_element(*LocatorsResultCalculate.CREDIT_OVERPAYMENT).text
    payments_loan_period = driver.find_element(*LocatorsResultCalculate.PAYMENTS_IOAN_PERIOD).text

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