from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class Starbucks_App:
    def __init__(self, driver: webdriver):
        """Initialize the Starbucks_App class with an Appium WebDriver instance."""
        self.driver = driver

    def starbucks_icon_click(self):
        """Click on the Starbucks icon on the device's home screen."""
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Starbucks").click()

    def order_now_button_click(self):
        """Click on the 'Order now' button on the Starbucks app home screen."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        order_now_button = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Order now"]')))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", order_now_button)  # Scroll into view
        order_now_button.click()

    def menu_bar_click(self):
        """Click on the menu bar to navigate to the menu options."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        menu_bar = wait.until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '1 of 4')))
        menu_bar.click()

    def frapuccino_beverages_category_click(self):
        """Click on the 'Frappuccino® Blended Beverages' category."""
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.TextView[@text="Frappuccino® Blended Beverages"]').click()

    def see_all_11_coffe_frapuccino_click(self):
        """Click on 'See all 11 Coffee Frappuccino® items' to view all items."""
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='See all 11 Coffee Frappuccino® items').click()

    def frapuccino_item_click(self):
        """Click on a specific Frappuccino item."""
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//o.TextValueSanitizer[@resource-id="com.starbucks.mobilecard:id/"]/android.view.View/android.view.View/android.view.View[4]/android.view.View').click()

    def item_name_text_app(self):
        """Retrieve the name of the selected item."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        item_name_text = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH,
                                              '//android.widget.TextView[@resource-id="com.starbucks.mobilecard:id/" and @text="Caramel Ribbon Crunch Frappuccino® Blended Beverage"]')))
        return item_name_text.text

    def item_calories_text_app(self):
        """Retrieve the calories information of the selected item."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        item_calories_text = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH,
                                              '//android.widget.TextView[@resource-id="com.starbucks.mobilecard:id/" and @text="470 calories"]')))
        return item_calories_text.text[:3]

    def allow_notifications_click(self):
        """Click on the button to allow notifications."""
        wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
        allow_notifications = wait.until(EC.visibility_of_element_located(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')))
        allow_notifications.click()

    def stores_button(self):
        """Retrieve the 'Stores' button element."""
        wait = WebDriverWait(self.driver, 10)
        stores_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Stores")))
        return stores_button

    def not_now_button_share_location_click(self):
        """Click on the 'Not now' button to skip sharing location."""
        self.driver.find_element(by=AppiumBy.ID, value="android:id/button2").click()

    def order_button_click(self):
        """Return the 'Order' button element."""
        wait = WebDriverWait(self.driver, 10)
        order_button = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Order')))
        order_button.click()

    def got_it_button_location_troubles_click(self):
        wait = WebDriverWait(self.driver, 10)
        got_it_button = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'android:id/button1')))
        got_it_button.click()

    def skip_choose_store_click(self):
        """Click on the 'skip' button to skip choosing a store."""
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//o.TextValueSanitizer[@content-desc="Choose a store"]/android.view.View/android.view.View/android.view.View/android.widget.Button').click()

    def yes_button_verify_skip_to_menu_click(self):
        """Click on the 'Yes' button to confirm skipping to the menu."""
        self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()

    def scan_button(self):
        """Return the 'Scan' button element."""
        return self.driver.find_element(by=AppiumBy.XPATH,
                                        value='(//android.widget.ImageView[@resource-id="com.starbucks.mobilecard:id/"])[4]')

    def allow_location_while_using_the_app_button_click(self):
        """Click on the 'While Using the App' button to allow location access while using the app."""
        self.driver.find_element(by=AppiumBy.ID,
                                 value='com.android.permissioncontroller:id/permission_allow_foreground_only_button')
