import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time


# Function to solve CAPTCHA using 2Captcha
def solve_captcha(api_key, site_key, page_url):
    captcha_data = {
        "key": api_key,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": page_url,
        "json": 1,
    }
    response = requests.post("http://2captcha.com/in.php", data=captcha_data)
    request_id = response.json()["request"]

    # Wait for CAPTCHA to be solved
    while True:
        response = requests.get(
            f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
        )
        if response.json()["status"] == 1:
            return response.json()["request"]
        elif response.json()["status"] == 0:
            raise Exception("CAPTCHA solving failed")


# Function to login
def login(driver, username, password):
    driver.get("https://secured.tfxi.sc/auth/login")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()


# Function to navigate to coin settlement
def navigate_to_coin_settlement(driver):
    driver.get("https://secured.tfxi.sc/account/coins-settlement/menu")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Coin Settlement"))
    ).click()


# Function to submit the settlement
def submit_settlement(driver, selling_amount):
    # Wait until 6:30 GMT
    wait_until_time(6, 30)

    # Check if the submit button is blue
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    if "blue" not in submit_button.get_attribute("class"):
        raise Exception("Submit button not available")

    # Copy the available amount and put it in selling amount
    amount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "amount"))
    )
    selling_amount.send_keys(amount.text)

    # Solve CAPTCHA
    captcha_token = solve_captcha(api_key, site_key, page_url)

    # Click submit button
    submit_button.click()

    # Handle any pop-up window (e.g., alert)
    WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()

    # Take a screenshot of the submission page
    driver.save_screenshot("submission.png")


# Function to wait until a specific time
def wait_until_time(hour, minute):
    target_time = datetime.utcnow().replace(
        hour=hour, minute=minute, second=0, microsecond=0
    )
    while datetime.utcnow() < target_time:
        time.sleep(1)


# Main function
def main():
    # Replace these variables with your actual values
    api_key = "72ff0d4cea274f07fd18074da41686c4"
    site_key = "6LejFR8TAAAAAIhwNUILaPgLC436CGfZjulor2ZQ"  # Provided site key
    page_url = "https://secured.tfxi.sc/auth/login"

    # Path to Chromedriver executable
    chromedriver_path = r"d:\Work Fiverr\code\py\chromedriver.exe"  # Replace this with the actual path to chromedriver.exe

    # Initialize Chromedriver service
    service = webdriver.chrome.service.Service(chromedriver_path)

    # Initialize Selenium webdriver
    driver = webdriver.Chrome(service=service)

    try:
        # Step 1: Login
        login(driver, "8189056", "Kldbae99!")

        # Step 2: Navigate to coin settlement
        navigate_to_coin_settlement(driver)

        # Step 3: Click on coin settlement
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Create"))
        ).click()

        # Step 4: Submit the settlement
        selling_amount = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "selling_amount"))
        )
        submit_settlement(driver, selling_amount)

        # Step 5: Bot goes to sleep until the next day 6:30 GMT
        wait_until_time(6, 30)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
