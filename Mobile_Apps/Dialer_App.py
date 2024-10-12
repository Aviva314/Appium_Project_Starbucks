from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Dialer_App:
    def __init__(self, driver: webdriver):
        """Initialize the Dialer_App class with an Appium WebDriver instance."""
        self.driver = driver

    def dialer_icon_click(self):
        """Click the dialer icon to open the Phone app."""
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Phone").click()

    def key_pad_click(self):
        """Wait for the key pad to become visible and click it."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        key_pad_element = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "key pad")))
        key_pad_element.click()

    def input_number_dialer(self, number: str):
        """Input the phone number into the dialer."""
        input_number = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/digits")
        input_number.clear()
        input_number.send_keys(number)

    def call_button_click(self):
        """Click the call button to initiate a phone call."""
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="dial").click()

    def end_call_button(self):
        """Wait for the end call button to become visible and return it."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        end_call_button = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.google.android.dialer:id/incall_end_call')))
        return end_call_button


