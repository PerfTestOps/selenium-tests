import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Provide a headless Chrome WebDriver instance for tests."""
    options = Options()
    options.add_argument("--headless")  # headless for Jenkins
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def timed_step(step_name, request, func):
    """Wrap an action with timing measurement and optional pytest reporting."""
    start = time.time()
    func()
    end = time.time()
    duration = end - start
    print(f"{step_name} response time: {duration:.2f} seconds")
    request.node.user_properties.append((step_name, duration))


def test_login(driver, request):
    """Verify login functionality and measure step timings."""
    wait = WebDriverWait(driver, 10)

    # Step 1: Open Login Page
    def open_login_page():
        driver.get("https://practicetestautomation.com/practice-test-login/")
    timed_step("Open Login Page", request, open_login_page)

    # Step 2: Enter Username
    def enter_username():
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys(os.getenv("TEST_USERNAME", "student"))
    timed_step("Enter Username", request, enter_username)

    # Step 3: Enter Password
    def enter_password():
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(os.getenv("TEST_PASSWORD", "Password123"))
    timed_step("Enter Password", request, enter_password)

    # Step 4: Click Submit
    def click_submit():
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_btn.click()
    timed_step("Click Submit", request, click_submit)

    # Step 5: Verify Success Message
    success_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "post-title"))).text
    print("Login message:", success_msg)

    # Assertion for Pytest
    assert "Logged In Successfully" in success_msg
