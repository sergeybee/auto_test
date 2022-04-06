from .pages.main_page import MainPage
import time

def test_url_creditcalculate_exists(browser):
	link = "http://creditcalculator.pointschool.ru"
	page = MainPage(browser, link)
	page.open()
	time.sleep(3)
	page.should_be_point_url()
	page.should_be_btn_calculate()


	