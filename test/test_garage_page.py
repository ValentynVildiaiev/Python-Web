from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from pages.home_page import HomePage


class TestGaragePage:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    # def teardown_method(self, method):
    # self.driver.quit()

    def adding_car_in_garage_page(self):
        page = HomePage(self.driver)
        page = page.click_sign_in_button()
        page = page.login_with_valid_user("validuser")
        assert (page.find_element(By.XPATH, "//a[@href='/panel/garage' and contains(@class, 'btn-sidebar')]")
                .is_displayed())
        return page

    def test_add_new_car(self):
        page = self.adding_car_in_garage_page()
        page = page.submit_car()
        time.sleep(1)
        assert page.check_added_car()
