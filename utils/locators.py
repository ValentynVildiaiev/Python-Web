from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.XPATH, "//a[@class='header_logo']")
    SIGNUP = (By.XPATH, "//button[text()='Sign up']")
    SIGNIN = (By.XPATH, "//button[contains(@class, 'header_signin')]")


class LoginPageLocators(object):
    EMAIL = (By.ID, "signinEmail")
    PASSWORD = (By.ID, "signinPassword")
    LOGIN = (By.XPATH, "//button[contains(text(),'Login')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class SignupPageLocators(object):
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER = (By.XPATH, "//button[text()='Register']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class GaragePageLocators(object):
    ADD_CAR = (By.XPATH, "//button[contains(text(),'Add car')]")
    CAR_BRAND = (By.XPATH, "//select[@id='addCarBrand']")
    CAR_AUDI = (By.XPATH, "//*[@id='addCarBrand']/option[1]")
    CAR_BMW = (By.XPATH, "//*[@id='addCarBrand']/option[2]")
    CAR_FORD = (By.XPATH, "//*[@id='addCarBrand']/option[3]")
    CAR_PORSCHE = (By.XPATH, "//*[@id='addCarBrand']/option[4]")
    CAR_FIAT = (By.XPATH, "//*[@id='addCarBrand']/option[5]")
    CAR_MILEAGE = (By.XPATH, "//input[@id='addCarMileage']")
    CAR_ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    CAR_CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    GARAGE_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Garage')]")
    CAR_ADDED_MESSAGE = (By.XPATH, "//p[contains(text(),'Car added')]")


class ExpensesLocators(object):
    FUEL_EXPENSES = (By.XPATH, "//a[@class='btn header-link'][normalize-space()='Fuel expenses']")
    ADD_EXPENSES = (By.XPATH, "//button[contains(text(),'Add an expense')]")
    CLOSE_EXPENSE_WIN = (By.XPATH, "//span[contains(text(),'×')]")
    EXPENSE_DATE = (By.ID, "addExpenseDate")
    ADD_MILEAGE = (By.ID, "addExpenseMileage")
    ADD_LITERS = (By.XPATH, "//input[@id='addExpenseLiters']")
    TOTAL_COST = (By.XPATH, "//input[@id='addExpenseTotalCost']")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    FUEL_EXPENSES_BUTTON = (By.XPATH, "//a[@href='/panel/expenses' and contains(@class, 'btn-sidebar')]")
    ADD_AN_EXPENSE_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
    ADDED_EXPENSE_CHECK = (By.XPATH, "//td[contains(text(),'16.02.2024')]")
    NEW_EXPENSE_ADDED = (By.XPATH, "//p[contains(text(),'Fuel expense added')]")


class CarLocators(object):
    ADD_FUEL_EXPENSE = (By.XPATH, "//button[contains(text(),'Add fuel expense')]")
    EDIT_BUTTON = (By.XPATH, "//span[@class='icon icon-edit']")
    EDIT_MILES = (By.XPATH, "//input[@name='miles']")
    UPDATE_BUTTON = (By.XPATH, "//button[contains(text(),'Update')]")
    CLOSE_EXPENSE_WIN = (By.XPATH, "//span[contains(text(),'×')]")
    EXPENSE_DATE = (By.ID, "addExpenseDate")
    ADD_MILEAGE = (By.ID, "addExpenseMileage")
    ADD_LITERS = (By.ID, "addExpenseLiters")
    TOTAL_COST = (By.ID, "addExpenseTotalCost")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    EDITCAR_MILEAGE = (By.ID, "addCarMileage")
    EDITCAR_DATE = (By.ID, "carCreationDate")
    REMOVE_CAR_BUTTON = (By.XPATH, "//button[contains(text(),'Remove car')]")
    SAVE_CAR_BUTTON = (By.XPATH, "//button[contains(text(),'Save')]")
    CANCEL_CAR_BUTTON = (By.XPATH, "//button[contains(text(),'Cancel')]")
