# store_details_page
from selenium import webdriver
from selenium.webdriver.common.by import By


class StoreDetailsPage:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the StoreDetailsPage class with a Selenium WebDriver instance."""
        self.driver = driver

    def get_phone_number(self):
        """Extract and return the phone number element of the selected store as text."""
        phone_number_element = self.driver.find_elements(By.CSS_SELECTOR, "div>a.sb-button>div>span")[1]
        return phone_number_element.text

    def opening_hours_rows(self):
        """Extract and return the opening hours per day elements of the selected store."""
        return self.driver.find_elements(By.CSS_SELECTOR, "div.px4>ul.schedule___SawQ4>li")

    def get_opening_day(self, i):
        """Extract and return the day element of the selected store after scrolling to make it visible."""
        day_element = self.opening_hours_rows()[i].find_elements(By.CSS_SELECTOR, "span")[0]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", day_element)  # Scroll into view
        return day_element.text

    def get_opening_hours(self, i):
        """Extract and return the opening hours element of the selected store after scrolling to make it visible."""
        hours_element = self.opening_hours_rows()[i].find_elements(By.CSS_SELECTOR, "span")[1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", hours_element)  # Scroll into view
        return hours_element.text
