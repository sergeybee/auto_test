from selenium.webdriver.support.ui import Select
from .locators import LocatorsDetailedCalculate
from .settings import SettingsDataSet as SD


# Ввод данных в блок "Детальный расчёт"
class DetailedCalculateCredit():

    # Заполняем поля анкеты подробного расчёта
    def enter_data_in_detailed_calculate(self):
        # Заполняем ФИО и паспортные данные
        second_name = self.browser.find_element(*LocatorsDetailedCalculate.SECOND_NAME_LOC)
        second_name.clear()
        second_name.send_keys(SD.SECOND_NAME)

        first_name = self.browser.find_element(*LocatorsDetailedCalculate.FIRST_NAME_LOC)
        first_name.clear()
        first_name.send_keys(SD.FIRST_NAME)

        middle_name = self.browser.find_element(*LocatorsDetailedCalculate.MIDDLE_NAME_LOC)
        middle_name.clear()
        middle_name.send_keys(SD.MIDDLE_NAME)

        passport = self.browser.find_element(*LocatorsDetailedCalculate.PASSPORT_LOC)
        passport.clear()
        passport.send_keys(SD.PASSPORT)

        issued_by = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_BY_LOC)
        issued_by.clear()
        issued_by.send_keys(SD.ISSUED_BY)

        issued_date = self.browser.find_element(*LocatorsDetailedCalculate.ISSUED_DATE_LOC)
        issued_date.clear()
        issued_date.send_keys(SD.ISSUED_DATE)

        # Выбор данных из выпадающего списка
        education = Select(self.browser.find_element(*LocatorsDetailedCalculate.EDUCATION_LOC))
        education.select_by_visible_text(SD.EDUCATION)

        seniority = Select(self.browser.find_element(*LocatorsDetailedCalculate.SENIORITY_LOC))
        seniority.select_by_visible_text(SD.SENIORITY)

        term_work_last_place = Select(self.browser.find_element(*LocatorsDetailedCalculate.TERM_WORK_LAST_PLACE_LOC))
        term_work_last_place.select_by_visible_text(SD.TERM_WORK_LAST_PLACE)

        confirmation_income_ndfl = Select(self.browser.find_element(*LocatorsDetailedCalculate.CONFIRMATION_INCOME_NDFL_LOC))
        confirmation_income_ndfl.select_by_visible_text(SD.CONFIRMATION_INCOME_NDFL)

        work_place_bank_area = Select(self.browser.find_element(*LocatorsDetailedCalculate.WORK_PLACE_BANK_AREA_LOC))
        work_place_bank_area.select_by_visible_text(SD.WORK_PLACE_BANK_AREA)

        net_income = self.browser.find_element(*LocatorsDetailedCalculate.NET_INCOME_LOC)
        net_income.clear()
        net_income.send_keys(SD.NET_INCOME)

        registration_place_bank_area = Select(self.browser.find_element(*LocatorsDetailedCalculate.REGISTRATION_PLACE_BANK_AREA_LOC))
        registration_place_bank_area.select_by_visible_text(SD.REGISTRATION_PLACE_BANK_AREA)

        previous_conviction = Select(self.browser.find_element(*LocatorsDetailedCalculate.PREVIOUS_CONFICTION_LOC))
        previous_conviction.select_by_visible_text(SD.PREVIOUS_CONFICTION)

        car = Select(self.browser.find_element(*LocatorsDetailedCalculate.CAR_LOC))
        car.select_by_visible_text(SD.CAR)

        real_estate = Select(self.browser.find_element(*LocatorsDetailedCalculate.REAL_ESTATE_LOC))
        real_estate.select_by_visible_text(SD.REAL_ESTATE)
