from pages.base_page import BasePage
from utils.locators import CarLocators
from utils.locators import ExpensesLocators


class CarPage(BasePage):
    def __init__(self, driver):
        self.locator = CarLocators
        super().__init__(driver)

    def car_add_fuel_expense(self):
        self.find_element(*self.locator.ADD_FUEL_EXPENSE).click()

    def report_date(self):
        self.find_element(*self.locator.EXPENSE_DATE).send_keys('18.01.2026')

    def report_milage(self):
        self.find_element(*self.locator.ADD_MILEAGE).send_keys('267')

    def new_liters(self):
        self.find_element(*self.locator.ADD_LITERS).send_keys('57')

    def total_cost(self):
        self.find_element(*self.locator.TOTAL_COST).send_keys('334')

    def click_add_button(self):
        self.find_element(*self.locator.SAVE_BUTTON).click()

    def click_cancel(self):
        self.find_element(*self.locator.CANCEL_BUTTON).click()

    def click_edit_button(self):
        self.find_element(*self.locator.EDIT_BUTTON).click()

    def edit_miles(self):
        self.find_element(*self.locator.EDIT_MILES).send_keys(255)

    def update_button(self):
        self.find_element(*self.locator.UPDATE_BUTTON).click()

