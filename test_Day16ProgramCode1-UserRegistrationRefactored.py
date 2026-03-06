import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """Setup and teardown for Chrome WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def log_action(action_name, func):
    """Helper to log start/end time and duration of an action."""
    start_time = time.time()
    print(f"[START] {action_name} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

    func()  # Execute the user action

    end_time = time.time()
    print(f"[END] {action_name} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    print(f"--> Duration: {end_time - start_time:.2f} seconds\n")


def test_fill_form_fields(driver):
    """Pytest-standard test function for filling form fields."""
    driver.get("https://testautomationpractice.blogspot.com/")

    # Fill Name field
    def fill_name():
        name_field = driver.find_element(By.ID, "name")
        name_field.send_keys("John Doe")
    log_action("Fill Name Field", fill_name)

    # Fill Email field
    def fill_email():
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("johndoe@example.com")
    log_action("Fill Email Field", fill_email)

    # Fill Phone field
    def fill_phone():
        phone_field = driver.find_element(By.ID, "phone")
        phone_field.send_keys("1234567890")
    log_action("Fill Phone Field", fill_phone)

    # Assertions to verify values entered
    assert driver.find_element(By.ID, "name").get_attribute("value") == "John Doe"
    assert driver.find_element(By.ID, "email").get_attribute("value") == "johndoe@example.com"
    assert driver.find_element(By.ID, "phone").get_attribute("value") == "1234567890"
