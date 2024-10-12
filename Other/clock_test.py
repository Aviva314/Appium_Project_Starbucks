# package=  com.google.android.deskclock
# act  = com.android.deskclock.DeskClock
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_server_url_local = 'http://localhost:4723/wd/hub'
capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
appActivity='com.android.deskclock.DeskClock',
appPackage= 'com.google.android.deskclock',
    platformVersion="35"

)


class clockTest(unittest.TestCase):


   def setUp(self)->None:
       self.driver = webdriver.Remote(appium_server_url_local, capabilities)

   def tearDown(self) -> None:
       if self.driver:
           self.driver.quit()

   def test1(self):
         clock_element = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.deskclock:id/digital_clock')
         time = clock_element.text
         print ('The Time is'+time)
         plus_button = self.driver.find_element(by=AppiumBy.ID,value= "com.google.android.deskclock:id/fab")
         plus_button.click()

