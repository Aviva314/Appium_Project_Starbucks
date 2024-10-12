from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Messages_App:
    def __init__(self, driver: webdriver):
        """Initialize the Messages_App class with an Appium WebDriver instance."""
        self.driver = driver

    def messages_icon_click(self):
        """Click on the Messages app icon to open the app."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        messages_icon = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Messages')))
        messages_icon.click()
        # self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Messages").click()

    def not_now_button_chat_on_computer_click(self):
        """Click the 'Not now' button in the chat on computer popup."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        start_chat_element = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Not now"]')))
        start_chat_element.click()

    def no_thanks_button_message_on_other_devices_click(self):
        """Click the 'No thanks' button in the message on other devices popup."""
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="No thanks"]').click()

    def start_new_chat_click(self):
        """Click on the 'Start chat' button to begin a new conversation."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        start_chat_element = wait.until(
            EC.visibility_of_element_located((AppiumBy.ID, "com.google.android.apps.messaging:id/start_chat_fab")))
        start_chat_element.click()

    def input_field_message(self, number: str):
        """Input a phone number in the 'To:' input field and select the contact."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        input_field = wait.until(
                EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText')))
        input_field.clear()  # Clear any pre-existing text
        input_field.send_keys(number)  # Input the phone number
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="ContactSuggestionList"]/android.view.View').click()

    def input_text_message(self, text: str):
        """Input a text message in the message input field."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        input_text = wait.until(
                EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText')))
        input_text.click()
        input_text.clear()
        input_text.send_keys(text)

    def send_sms_button_click(self):
        """Click the 'Send SMS' button to send the text message."""
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send SMS").click()

    def texting_with_element(self):
        """Return the element indicating texting with the selected contact."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        input_text = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="message_text" and @text="Texting with +420 235 013 550 (SMS/MMS)"]')))
        return input_text

    def text_bubble_element(self):
        """Return the element representing the latest text bubble in the conversation."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        text_bubble = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="message_list"]/android.view.View[1]/android.view.View[1]')))
        return text_bubble



