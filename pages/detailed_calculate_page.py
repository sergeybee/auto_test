from base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from locators import LocatorsDetailedCalculate


# Вводим данные в блок ДЕТАЛЬНЫЙ РАСЧЕТ
class DetailedCalculateCredit(BasePage):

	def entering_data_in_detailed_calculate():

	    second_name = driver.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC)
	    second_name.clear()
	    second_name.send_keys(SECOND_NAME)
	    
	    first_name = driver.find_element(*LocatorsDetailedCalculate.FIRST_NAME_LOC)
	    first_name.clear()
	    first_name.send_keys(FIRST_NAME)

	    middle_name = driver.find_element(*LocatorsDetailedCalculate.MIDDLE_NAME_LOC)
	    middle_name.clear()
	    middle_name.send_keys(MIDDLE_NAME)

	    passport = driver.find_element(*LocatorsDetailedCalculate.PASSPORT_LOC)
	    passport.clear()
	    passport.send_keys(PASSPORT)

	    issued_by = driver.find_element(*LocatorsDetailedCalculate.ISSUED_BY_LOC)
	    issued_by.clear()
	    issued_by.send_keys(ISSUED_BY)
	    
	    issued_date = driver.find_element(*LocatorsDetailedCalculate.ISSUED_DATE_LOC)
	    issued_date.clear()
	    issued_date.send_keys(ISSUED_DATE)

	    # Выбор данных из выпадающего списка

	    education = Select(driver.find_element(*LocatorsDetailedCalculate.EDUCATION_LOC))                                        # Образование
	    education.select_by_visible_text(EDUCATION)
	    
	    seniority = Select(driver.find_element(*LocatorsDetailedCalculate.SENIORITY_LOC))                                        # Общий трудовой стаж
	    seniority.select_by_visible_text(SENIORITY)

	    term_work_last_place = Select(driver.find_element(*LocatorsDetailedCalculate.TERM_WORK_LAST_PLACE_LOC))                  # Срок работы на последнем месте
	    term_work_last_place.select_by_visible_text(TERM_WORK_LAST_PLACE)

	    confirmation_income_ndfl = Select(driver.find_element(*LocatorsDetailedCalculate.CONFIRMATION_INCOME_NDFL_LOC))          # Подтверждение дохода справкой 2НДФЛ
	    confirmation_income_ndfl.select_by_visible_text(CONFIRMATION_INCOME_NDFL)

	    work_place_bank_area = Select(driver.find_element(*LocatorsDetailedCalculate.WORK_PLACE_BANK_AREA_LOC_LOC))                  # Место работы в регионе регистрации банка?
	    work_place_bank_area.select_by_visible_text(WORK_PLACE_BANK_AREA)

	    net_income = driver.find_element(*LocatorsDetailedCalculate.NET_INCOME_LOC)                        # Чистый доход в месяц
	    net_income.clear()
	    net_income.send_keys(NET_INCOME)

	    registration_place_bank_area = Select(driver.find_element(*LocatorsDetailedCalculate.REGISTRATION_PLACE_BANK_AREA_LOC))  # Место прописки в регионе регистрации банка?
	    registration_place_bank_area.select_by_visible_text(REGISTRATION_PLACE_BANK_AREA)

	    previous_conviction = Select(driver.find_element(*LocatorsDetailedCalculate.PREVIOUS_CONFICTION_LOC_LOC))                    # Есть ли у вас судимость?
	    previous_conviction.select_by_visible_text(PREVIOUS_CONFICTION)

	    car = Select(driver.find_element(*LocatorsDetailedCalculate.CAR_LOC))                                                    # Есть ли у вас в собственности автомобиль?
	    car.select_by_visible_text(CAR)

	    real_estate = Select(driver.find_element(*LocatorsDetailedCalculate.REAL_ESTATE_LOC))                                    # Есть ли у вас в собственности недвижимость?
	    real_estate.select_by_visible_text(REAL_ESTATE)
	    