from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Google_App:
    def __init__(self, driver: webdriver):
        """Initialize the Google_App class with an Appium WebDriver instance."""
        self.driver = driver

    def Chrome_icon_click(self):
        """Click on the Chrome icon to open the Chrome browser."""
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome").click()

    def google_logo_click(self):
        """Click on the Google logo on the search screen."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        google_logo = wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.Image')))
        google_logo.click()

    def google_homepage_click(self):
        """Click on the homepage icon on the search screen."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        homepage = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Open the home page')))
        homepage.click()

    def search_box_click(self):
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        search_box = wait.until(
            EC.visibility_of_element_located((AppiumBy.ID, 'com.android.chrome:id/search_box_text')))
        search_box.click()

    def input_search_or_type_url_bar_from_main_page(self, search: str):
        """Enter a search term into the Chrome search bar from the main Google page and press Enter."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        input_search = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.android.chrome:id/url_bar')))
        input_search.send_keys(search)
        self.driver.press_keycode(66)  # 66 is the keycode for "Enter"

    def input_search_value_from_search_page(self, search: str):
        """Enter a search term into the Chrome search bar from an existing search page and press Enter."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        input_search = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                                    '//android.webkit.WebView[@text="Google"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText')))
        input_search.click()
        input_search.send_keys(search)
        self.driver.press_keycode(66)  # 66 is the keycode for "Enter"

    def delete_current_search_button_click(self):
        """Click the button to delete the current search."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        call_delete_button = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="ניקוי החיפוש"]')))
        call_delete_button.click()

    def return_arrow_button_click(self):
        """Click the return arrow button to go back to the previous screen."""
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="הקודם"]').click()

    def call_store_click(self):
        """Click the phone icon to call the store."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        call_store = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="להתקשרות"]')))
        call_store.click()

    def store_phone_number_text(self):
        """Return the store's phone number as text."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        phone_number = wait.until(
            EC.visibility_of_element_located((AppiumBy.ID, 'com.google.android.dialer:id/digits')))
        return phone_number.text.replace(" ", "")
