# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestOpenwebpageloginaddcar():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_openwebpageloginaddcar(self):
        self.driver.get("https://qauto.forstudy.space/")
        self.driver.set_window_size(1472, 1023)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-white").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-white")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "signinEmail").send_keys("yuri.gr.bond@gmail.com")
        self.driver.find_element(By.ID, "signinPassword").send_keys("E5YvjATAPb7@Uz4")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sidebar > .btn:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sidebar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sidebar > .btn:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "addCarMileage").click()
        self.driver.find_element(By.ID, "addCarMileage").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".car_add-expense").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".car_add-expense")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "addExpenseMileage").click()
        self.driver.find_element(By.ID, "addExpenseMileage").click()
        self.driver.find_element(By.ID, "addExpenseMileage").send_keys("1001")
        self.driver.find_element(By.ID, "addExpenseLiters").click()
        self.driver.find_element(By.ID, "addExpenseLiters").send_keys("50")
        self.driver.find_element(By.ID, "addExpenseTotalCost").click()
        self.driver.find_element(By.ID, "addExpenseTotalCost").send_keys("29")
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-9").click()
        self.driver.find_element(By.ID, "userNavDropdown").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(6)").click()
