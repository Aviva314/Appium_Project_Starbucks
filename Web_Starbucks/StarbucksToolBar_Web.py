# store_toolbar
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class StarbucksToolBar:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the StarbucksToolBar class with a Selenium WebDriver instance."""
        self.driver = driver

    def go_to_store_locator(self):
        """Navigate to the store locator page by clicking on the 'Find a store' link."""
        store_locator_link = self.driver.find_element(By.LINK_TEXT, "Find a store")
        store_locator_link.click()



