import time

from pages.base_page import BasePage
from utils.locators import ExpensesLocators


class ExpensesPage(BasePage):
    def __init__(self, driver):
        self.locator = ExpensesLocators
        super().__init__(driver)

    def add_expenses(self):
        self.find_element(*self.locator.ADD_EXPENSES).click()

    def add_report_date(self):
        self.find_element(*self.locator.EXPENSE_DATE).click()
        self.find_element(*self.locator.EXPENSE_DATE).clear()
        self.find_element(*self.locator.EXPENSE_DATE).send_keys("16.02.2024")

    def edit_mileage(self):
        self.find_element(*self.locator.ADD_MILEAGE).click()
        self.find_element(*self.locator.ADD_MILEAGE).clear()
        self.find_element(*self.locator.ADD_MILEAGE).send_keys("175")

    def add_liters(self):
        self.find_element(*self.locator.ADD_LITERS).click()
        self.find_element(*self.locator.ADD_LITERS).send_keys("55")

    def total_cost(self):
        self.find_element(*self.locator.TOTAL_COST).click()
        self.find_element(*self.locator.TOTAL_COST).send_keys("250")

    def add_button(self):
        self.find_element(*self.locator.ADD_BUTTON).click()

    def side_expenses_button(self):
        self.find_element(*self.locator.FUEL_EXPENSES_BUTTON).click()

    def add_an_expense_button(self):
        self.find_element(*self.locator.ADD_AN_EXPENSE_BUTTON).click()

    def cancel_button(self):
        self.find_element(*self.locator.CANCEL_BUTTON).click()

    def added_expense(self):
        return self.find_element(*self.locator.NEW_EXPENSE_ADDED).is_displayed()

    def add_expense_to_car(self):
        self.side_expenses_button()
        time.sleep(2)
        self.add_an_expense_button()
        self.add_report_date()
        time.sleep(2)
        self.edit_mileage()
        time.sleep(2)
        self.add_liters()
        time.sleep(2)
        self.total_cost()
        time.sleep(2)
        self.add_button()
        return self

    def check_added_expense(self):
        return self.added_expense()
