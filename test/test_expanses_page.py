import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage


class TestExpansesPage:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def adding_expense_to_a_car(self):
        page = HomePage(self.driver)
        page = page.click_sign_in_button()
        page = page.login_with_valid_user("validuser")
        assert (page.find_element(By.XPATH, "//a[@href='/panel/garage' and contains(@class, 'btn-sidebar')]")
                .is_displayed())
        return page

    def test_add_new_expenses(self):
        time.sleep(2)
        page = self.adding_expense_to_a_car()
        page = page.add_expense_to_car()
        time.sleep(1)
        assert page.check_added_expense()

