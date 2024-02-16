import time

from pages.base_page import BasePage
from utils.locators import GaragePageLocators


class GaragePage(BasePage):
    def __init__(self, driver):
        self.locator = GaragePageLocators
        super().__init__(driver)

    def click_add_new_car_button(self):
        self.find_element(*self.locator.ADD_CAR).click()

    def add_car_brand_audi(self):
        self.find_element(*self.locator.CAR_BRAND).click()

    def add_model_audi_tt(self):
        self.find_element(*self.locator.CAR_AUDI).click()

    def add_car_brand_bmw(self):
        self.find_element(*self.locator.CAR_BRAND).click()

    def add_model_bmw_3(self):
        self.find_element(*self.locator.CAR_BMW).click()

    def add_car_brand_ford(self):
        self.find_element(*self.locator.CAR_BRAND).click()

    def add_model_audi_fiesta(self):
        self.find_element(*self.locator.CAR_FORD).click()

    def add_car_brand_porsche(self):
        self.find_element(*self.locator.CAR_BRAND).click()

    def add_model_audi_911(self):
        self.find_element(*self.locator.CAR_PORSCHE).click()

    def add_car_brand_fiat(self):
        self.find_element(*self.locator.CAR_BRAND).click()

    def add_model_audi_palio(self):
        self.find_element(*self.locator.CAR_FIAT).click()

    def input_mileage(self):
        self.find_element(*self.locator.CAR_MILEAGE).click()
        self.find_element(*self.locator.CAR_MILEAGE).send_keys("5")

    def click_save_new_car_button(self):
        self.find_element(*self.locator.CAR_ADD_BUTTON).click()

    def car_added_message(self):
        return self.find_element(*self.locator.CAR_ADDED_MESSAGE).is_displayed()

    def submit_car(self):
        self.click_add_new_car_button()
        self.input_mileage()
        time.sleep(2)
        self.click_save_new_car_button()
        return self

    def check_added_car(self):
        return self.car_added_message()

