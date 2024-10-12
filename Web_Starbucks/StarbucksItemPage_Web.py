# Item_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ItemPage:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the ItemPage class with a Selenium WebDriver instance."""
        self.driver = driver

    def item_name_text(self):
        """Return the name of the item as text."""
        return self.driver.find_element(By.CSS_SELECTOR, '[data-e2e="product-name"]').text

    def item_calories_text(self):
        """Return the calorie information of the item as text."""
        return self.driver.find_element(By.CLASS_NAME, 'caloriesLeftOffset___bmLU8').text

