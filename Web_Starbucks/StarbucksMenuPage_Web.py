# Menu_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MenuPage:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the MenuPage class with a Selenium WebDriver instance."""
        self.driver = driver

    def go_to_drinks_menu_click(self):
        """Navigate to the drinks menu by clicking the first global navigation link."""
        self.driver.find_elements(By.CLASS_NAME, "sb-globalNav__desktopLink")[0].click()

    def frapuccino_beverages_category_click(self):
        """Scroll to the Frappuccino® Blended Beverages category and click on it."""
        category_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.grid>div>[data-e2e="Frappuccino® Blended Beverages"]')))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", category_element)
        category_element.click()

    def frapuccino_item_click(self):
        """Scroll to the Caramel Ribbon Crunch Frappuccino® Blended Beverage item and click on it."""
        item_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'div.grid>div>div>a[data-e2e="Caramel Ribbon Crunch Frappuccino® Blended Beverage"]')))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", item_element)
        item_element.click()
