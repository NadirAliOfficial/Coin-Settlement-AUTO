from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.recaptchav2proxyless import *
import os
from datetime import datetime, timedelta
import time


# Function to solve CAPTCHA using AntiCaptcha
def solve_captcha(site_key, page_url):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("72ff0d4cea274f07fd18074da41686c4")
    solver.set_website_url(page_url)
    solver.set_website_key(site_key)
    solver.set_soft_id(0)
    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        return g_response
    else:
        raise Exception("CAPTCHA solving failed")


# Function to login
def login(driver, username, password):
    try:
        driver.get("https://secured.tfxi.sc/auth/login")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        ).send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginButton").click()
    except Exception as e:
        raise Exception(f"Error occurred during login: {str(e)}")


# Function to navigate to coin settlement
def navigate_to_coin_settlement(driver):
    try:
        driver.get("https://secured.tfxi.sc/account/coins-settlement/menu")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[@src='https://secured.tfxi.sc/images/icons/coins-settlement.png']",
                )
            )
        ).click()
        current_directory = os.getcwd()
        driver.save_screenshot(os.path.join(current_directory, "submission2.png"))

        target_element = driver.find_element(By.ID, "requestCoinAmountInput")

        target_element.send_keys("1,023.372")

        submit_button = driver.find_element(By.ID, "submitCoinSettlementButton")
        submit_button.click()

    except Exception as e:
        raise Exception(f"Error occurred while navigating to coin settlement: {str(e)}")


# Function to submit the settlement
def submit_settlement(driver, site_key, page_url):
    try:
        # Solve CAPTCHA
        captcha_response = solve_captcha(site_key, page_url)

        # Set the CAPTCHA response in the input field
        captcha_input = driver.find_element_by_id("g-recaptcha-response")
        captcha_input.send_keys(captcha_response)

        # Click submit button
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "submitCoinSettlementButton"))
        )
        submit_button.click()
    except Exception as e:
        raise Exception(f"Error occurred while submitting settlement: {str(e)}")


# Function to wait until a specific time
def wait_until_time(hour, minute):
    try:
        target_time = datetime.utcnow().replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )
        while datetime.utcnow() < target_time:
            time.sleep(1)
    except Exception as e:
        raise Exception(f"Error occurred during wait time: {str(e)}")


# Main function
def main():
    # Replace these variables with your actual values
    username = "8189056"
    password = "Kldbae999!!!"
    site_key = "6LejFR8TAAAAAIhwNUILaPgLC436CGfZjulor2ZQ"
    page_url = "https://secured.tfxi.sc/account/coins-settlement/create"
    chromedriver_path = r"F:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    # Initialize Chromedriver service
    service = webdriver.chrome.service.Service(chromedriver_path)

    # Initialize Selenium webdriver
    driver = webdriver.Chrome(service=service)

    try:
        # Login
        login(driver, username, password)
        # Navigate to coin settlement
        navigate_to_coin_settlement(driver)
        # Click on coin settlement
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Create"))
        ).click()
        # Submit the settlement
        submit_settlement(driver, site_key, page_url)
        # Solve CAPTCHA
        captcha_response = solve_captcha(site_key, page_url)
        # Set the CAPTCHA response in the input field
        captcha_input = driver.find_element_by_id("g-recaptcha-response")
        captcha_input.send_keys(captcha_response)
        print(captcha_response)
        # Handle unexpected alert
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert Text: {alert_text}")
            time.sleep(2)
            alert.accept()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    finally:
        current_directory = os.getcwd()
        driver.save_screenshot(os.path.join(current_directory, "Submission.png"))
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    main()
