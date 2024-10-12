from unittest import TestCase
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Mobile_Apps.Dialer_App import Dialer_App
from Mobile_Apps.Messages_App import Messages_App
from time import sleep

appium_server_url_local = 'http://localhost:4723/wd/hub'

capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    # appActivity='com.google.android.apps.nexuslauncher.NexusLauncherActivity',
    # appPackage='com.google.android.apps.nexuslauncher',
    platformVersion="35"
)

dialer_capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    appActivity='com.google.android.dialer.extensions.GoogleDialtactsActivity',
    appPackage='com.google.android.dialer',
    platformVersion="35"
)

messages_capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    appActivity='com.google.android.apps.messaging.ui.ConversationListActivity',
    appPackage="com.google.android.apps.messaging",
    platformVersion="35"
)


class Main_App_Test(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url_local, capabilities)
        self.dialer = Dialer_App(self.driver)
        self.messages = Messages_App(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_dialer_with_functions(self):
        self.dialer.dialer_icon_click()
        self.dialer.key_pad_click()

    def test_dialer_icon_click(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Phone").click()
        sleep(4)
        dialer_element = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_fab')
        dialer_element.click()

    def test_dial_number(self):
        self.dialer.dialer_icon_click()
        self.dialer.key_pad_click()
        self.dialer.input_number_dialer("0508193998")
        self.dialer.call_button_click()

    def test_messages_with_functions(self):
        self.messages.messages_icon_click()
        self.messages.start_new_chat_click()

    def test_messages_icon_click(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Messages").click()
        sleep(3)
        start_chat_element = self.driver.find_element(by=AppiumBy.ID,
                                                      value="com.google.android.apps.messaging:id/start_chat_fab")
        start_chat_element.click()
