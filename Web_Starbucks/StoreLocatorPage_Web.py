# store_locator_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class StoreLocatorPage:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the StoreLocatorPage class with a Selenium WebDriver instance."""
        self.driver = driver

    def search_store(self, location):
        """Search for a store by its location using the search input field."""
        search_input = self.driver.find_element(By.CSS_SELECTOR, '[name="place"]')
        search_input.clear()
        search_input.send_keys(location + Keys.ENTER)

    def select_store_info(self):
        """Select the store from the search results by scrolling to the store element and clicking on its link."""
        # Use JavaScript to scroll to the element if it’s not in view
        store_link = self.driver.find_element(By.CSS_SELECTOR,
                                              "article.base___JrMLA:nth-child(6) > div:nth-child(2) > div:nth-child(2) > "
                                              "div:nth-child(1) > a:nth-child(2) > svg:nth-child(1)")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", store_link)

        # Additional wait to ensure the element is interactable
        ActionChains(self.driver).move_to_element(store_link).click(store_link).perform()

        # Alternatively, you can directly use JavaScript to click
        # self.driver.execute_script("arguments[0].click();", store_link)
