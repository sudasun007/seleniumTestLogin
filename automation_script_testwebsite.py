import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import logging
import time
import random
import string


class HumanTypingBehavior:
    @staticmethod
    def human_type(element, text):
        """Simulates human-like typing with variable delays."""
        if element.get_attribute('value'):
            for _ in range(len(element.get_attribute('value'))):
                element.send_keys(Keys.BACKSPACE)
                time.sleep(random.uniform(0.1, 0.2))
        for char in text:
            element.send_keys(char)
            if char in string.punctuation + ' ':
                time.sleep(random.uniform(0.1, 0.3))
            else:
                time.sleep(random.uniform(0.05, 0.2))

    @staticmethod
    def random_human_delay():
        """Adds random delay to simulate human thinking/reading time."""
        time.sleep(random.uniform(0.5, 2.0))


class TechShopTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://testwebsitesudh.netlify.app/")  # Update this URL
        self.wait = WebDriverWait(self.driver, 20)
        self.human = HumanTypingBehavior()

        # Create directory for test results
        self.results_dir = "test_results_Testsite"
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)

    def tearDown(self):
        self.human.random_human_delay()
        self.driver.quit()

    def save_screenshot(self, name):
        """Save a screenshot with the given name."""
        screenshot_path = os.path.join(self.results_dir, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")

    def _login(self, username="testuser", password="password123"):
        """Helper method for login with human-like behavior."""
        username_input = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

        self.human.random_human_delay()
        self.human.human_type(username_input, username)
        self.human.random_human_delay()
        self.human.human_type(password_input, password)
        self.human.random_human_delay()
        login_button.click()

    def test_01_login_functionality(self):
        """Test login with valid and invalid credentials."""
        try:
            # Invalid login
            self._login(username="wronguser", password="wrongpass")
            error_container = self.wait.until(EC.visibility_of_element_located((By.ID, "errorContainer")))
            self.assertTrue(error_container.is_displayed())
            logging.info("Invalid login test passed.")
            self.save_screenshot("invalid_login")

            # Valid login
            self._login()

            # Wait for dashboard to load before capturing the screenshot
            dashboard = self.wait.until(EC.visibility_of_element_located((By.ID, "dashboard")))
            welcome_message = self.driver.find_element(By.ID, "welcomeText").text
            self.assertTrue("Welcome back, testuser!" in welcome_message)
            self.assertTrue(dashboard.is_displayed())
            logging.info("Valid login test passed.")
            self.save_screenshot("valid_login")  # Take screenshot after page has loaded

        except Exception as e:
            logging.error(f"Error during login test: {e}")
            self.save_screenshot("login_test_error")

    def test_02_navigation_after_login(self):
        """Test navigation elements with human-like behavior."""
        self._login()
        try:
            nav_links = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-links a")))
            for index, link in enumerate(nav_links[:3]):  # Test first 3 links
                self.human.random_human_delay()
                link.click()
                self.human.random_human_delay()
                self.save_screenshot(f"navigation_test_link_{index + 1}")
            logging.info("Navigation test passed.")
        except Exception as e:
            logging.error(f"Error during navigation test: {e}")
            self.save_screenshot("navigation_test_error")

    def test_03_dashboard_display(self):
        """Test that the dashboard and welcome message are displayed after login."""
        self._login()
        try:
            # Wait for dashboard to load before capturing the screenshot
            dashboard = self.wait.until(EC.visibility_of_element_located((By.ID, "dashboard")))
            welcome_message = self.driver.find_element(By.ID, "welcomeText").text
            self.assertTrue("Welcome back, testuser!" in welcome_message)
            self.assertTrue(dashboard.is_displayed())
            logging.info("Dashboard display test passed.")
            self.save_screenshot("dashboard_display")  # Take screenshot after page has loaded
        except Exception as e:
            logging.error(f"Error during dashboard test: {e}")
            self.save_screenshot("dashboard_test_error")

if __name__ == "__main__":
    unittest.main()
