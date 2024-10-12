from unittest import TestCase
from Globals.Globals import *

from appium import webdriver as appium_webdriver

from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.service import Service

from Mobile_Apps.Starbucks_App import Starbucks_App
from Mobile_Apps.Dialer_App import Dialer_App
from Mobile_Apps.Messages_App import Messages_App
from Mobile_Apps.Google_Chrome_App import Google_App
from Web_Starbucks.StarbucksToolBar_Web import StarbucksToolBar
from Web_Starbucks.StoreLocatorPage_Web import StoreLocatorPage
from Web_Starbucks.StoreDetailsPage_Web import StoreDetailsPage
from Web_Starbucks.StarbucksMenuPage_Web import MenuPage
from Web_Starbucks.StarbucksItemPage_Web import ItemPage
from Globals.Item_class import Item

from time import sleep


class StarbucksTest(TestCase):

    def setUp(self) -> None:
        # Setup Appium (Mobile) Driver
        self.mobile_driver = appium_webdriver.Remote(appium_server_url_local, capabilities)

        # Setup Selenium (Web) Driver
        service_chrome = Service(r"C:\Users\aviva\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.web_driver = selenium_webdriver.Chrome(service=service_chrome)

        self.web_driver.get(base_url)
        self.web_driver.maximize_window()
        self.web_driver.implicitly_wait(10)  # Implicit wait for Selenium WebDriver

        # Page Object Model (POM) Initializations
        self.app_starbucks = Starbucks_App(self.mobile_driver)
        self.app_dialer = Dialer_App(self.mobile_driver)
        self.app_messages = Messages_App(self.mobile_driver)
        self.app_google = Google_App(self.mobile_driver)
        self.web_tool_bar = StarbucksToolBar(self.web_driver)
        self.web_store_locator_page = StoreLocatorPage(self.web_driver)
        self.web_store_details_page = StoreDetailsPage(self.web_driver)
        self.web_menu_page = MenuPage(self.web_driver)
        self.web_item_page = ItemPage(self.web_driver)

    def tearDown(self) -> None:
        # Quit both drivers
        if self.mobile_driver:
            sleep(3)
            self.mobile_driver.terminate_app("com.google.android.dialer")
            self.mobile_driver.terminate_app("com.google.android.apps.messaging")
            self.mobile_driver.terminate_app("com.android.chrome")
            self.mobile_driver.terminate_app("com.starbucks.mobilecard")
        if self.web_driver:
            self.web_driver.quit()

    def test_1_dial_store_when_open(self):
        # Go to the store locator page
        self.web_tool_bar.go_to_store_locator()

        # Search for the store in Prague
        self.web_store_locator_page.search_store("Prague")

        # Select the store information
        self.web_store_locator_page.select_store_info()

        # Get the store's phone number
        phone_number = self.web_store_details_page.get_phone_number().replace(" ", "")
        print(phone_number)

        opening_hours = {}
        for i in range(len(self.web_store_details_page.opening_hours_rows())):
            day = self.web_store_details_page.get_opening_day(i)
            hours_per_day = self.web_store_details_page.get_opening_hours(i)
            opening_hours[day] = hours_per_day

        if is_store_open(opening_hours):
            print("The store is open.")
            print(f"Opening hours:\n{opening_hours}")
            self.app_dialer.dialer_icon_click()
            self.app_dialer.key_pad_click()
            self.app_dialer.input_number_dialer(phone_number)
            self.app_dialer.call_button_click()
            end_call_button = self.app_dialer.end_call_button()
            self.assertEqual(type(end_call_button), appium_webdriver.WebElement)
        else:
            print("Store is closed. No call initiated.")

    def test_2_message_store_when_close(self):
        # Go to the store locator page
        self.web_tool_bar.go_to_store_locator()

        # Search for the store in Prague
        self.web_store_locator_page.search_store("Prague")

        # Select the store information
        self.web_store_locator_page.select_store_info()

        # Get the store's phone number
        phone_number = self.web_store_details_page.get_phone_number().replace(" ", "")
        print(phone_number)

        opening_hours = {}
        for i in range(len(self.web_store_details_page.opening_hours_rows())):
            day = self.web_store_details_page.get_opening_day(i)
            hours_per_day = self.web_store_details_page.get_opening_hours(i)
            opening_hours[day] = hours_per_day

        # Check if the store is open
        if not is_store_open(opening_hours):
            print("The store is closed. Sending an SMS...")
            print(f"Opening hours:\n{opening_hours}")

            # Open the Messages app and compose a new message
            self.app_messages.messages_icon_click()

            # Handle any popups
            # self.app_messages.not_now_button_chat_on_computer_click()
            # self.app_messages.no_thanks_button_message_on_other_devices_click()

            # Start a new chat
            self.app_messages.start_new_chat_click()

            # Input the store's phone number
            self.app_messages.input_field_message(phone_number)

            # Compose the text message
            text_message = ("Hello, I would like to know if the 'Iced Caramel Macchiato'"
                            " is available for order at your Starbucks branch?")
            self.app_messages.input_text_message(text_message)

            # Send the SMS
            self.app_messages.send_sms_button_click()
            # self.assertEqual("Texting with +420 235 013 550 (SMS/MMS)", self.app_messages.texting_with_element().text)
            self.assertEqual(type(self.app_messages.text_bubble_element()), appium_webdriver.WebElement)
        else:
            print("Store is open. Communication should be via phone call.")

    def test_3_dial_store_and_send_message_when_open(self):
        # Go to the store locator page
        self.web_tool_bar.go_to_store_locator()

        # Search for the store in Prague
        self.web_store_locator_page.search_store("Prague")

        # Select the store information
        self.web_store_locator_page.select_store_info()

        # Get the store's phone number
        phone_number = self.web_store_details_page.get_phone_number().replace(" ", "")
        print(phone_number)

        opening_hours = {}
        for i in range(len(self.web_store_details_page.opening_hours_rows())):
            day = self.web_store_details_page.get_opening_day(i)
            hours_per_day = self.web_store_details_page.get_opening_hours(i)
            opening_hours[day] = hours_per_day

        if is_store_open(opening_hours):
            print("The store is open.")
            print(f"Opening hours:\n{opening_hours}")
            # Make a call to the store during business hours, and end the call when it's over.
            self.app_dialer.dialer_icon_click()
            self.app_dialer.key_pad_click()
            self.app_dialer.input_number_dialer(phone_number)
            self.app_dialer.call_button_click()
            end_call_button = self.app_dialer.end_call_button()
            self.assertEqual(type(end_call_button), appium_webdriver.WebElement)
            end_call_button.click()
            self.mobile_driver.press_keycode(3)

            # Send SMS the store's number, during opening hours

            # Open the Messages app and compose a new message
            self.app_messages.messages_icon_click()

            # Start a new chat
            self.app_messages.start_new_chat_click()

            # Input the store's phone number
            self.app_messages.input_field_message(phone_number)

            # Compose the text message
            text_message = ("Hi, I wanted to check if the 'Vanilla Sweet Cream Cold Brew' is available for order at "
                            "your Starbucks store?")
            self.app_messages.input_text_message(text_message)

            # Send the SMS
            self.app_messages.send_sms_button_click()
            # self.assertEqual("Texting with +420 235 013 550 (SMS/MMS)", self.app_messages.texting_with_element().text)
            self.assertEqual(type(self.app_messages.text_bubble_element()), appium_webdriver.WebElement)
        else:
            print("The shop is closed. Calls and SMS are not available.")

    def test_4_store_number_from_site_vs_browser(self):

        # Go to the store locator page
        self.web_tool_bar.go_to_store_locator()

        # Search for the store in Prague
        self.web_store_locator_page.search_store("Prague")

        # Select the store information
        self.web_store_locator_page.select_store_info()

        # Get the store's phone number
        phone_number_from_store_site = self.web_store_details_page.get_phone_number().replace(" ", "")
        print(f"phone_number_from_Starbucks_site: {phone_number_from_store_site}")

        # Go to Chrome browser on the phone and search for Starbucks branch in Prague Spalena street
        self.app_google.Chrome_icon_click()
        self.app_google.google_homepage_click()
        self.app_google.search_box_click()
        self.app_google.input_search_or_type_url_bar_from_main_page("starbucks prague spalena")

        # Retrieve the store's phone number fom the browser
        self.app_google.call_store_click()
        phone_number_from_browser = self.app_google.store_phone_number_text()
        print(f"phone_number_from_browser: {phone_number_from_browser}")

        self.assertEqual(phone_number_from_store_site, phone_number_from_browser)

    def test_5_compare_item_web_vs_app(self):
        # Get item details from web
        self.web_menu_page.go_to_drinks_menu_click()
        self.web_menu_page.frapuccino_beverages_category_click()
        self.web_menu_page.frapuccino_item_click()

        web_item_name = self.web_item_page.item_name_text()
        web_item_calories = self.web_item_page.item_calories_text()
        print(f"Web item name: {web_item_name}\nWeb item calories: {web_item_calories}")

        # Get item details from the app
        self.app_starbucks.starbucks_icon_click()
        self.app_starbucks.order_button_click()
        # self.app_starbucks.got_it_button_location_troubles_click()
        self.app_starbucks.skip_choose_store_click()
        self.app_starbucks.yes_button_verify_skip_to_menu_click()
        self.app_starbucks.menu_bar_click()
        self.app_starbucks.frapuccino_beverages_category_click()
        self.app_starbucks.see_all_11_coffe_frapuccino_click()
        self.app_starbucks.frapuccino_item_click()

        app_item_name = self.app_starbucks.item_name_text_app()
        app_item_calories = self.app_starbucks.item_calories_text_app()
        print(f"App item name: {app_item_name}\nApp item calories: {app_item_calories}")

        # Create Item objects
        web_item = Item(web_item_name, web_item_calories)
        app_item = Item(app_item_name, app_item_calories)

        # Assert that both items are equal
        self.assertEqual(web_item, app_item)
        print("Item details match across web and app.")

