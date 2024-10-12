from selenium import webdriver
from Web_Starbucks.StarbucksToolBar_Web import StarbucksToolBar
from Web_Starbucks.StoreLocatorPage_Web import StoreLocatorPage
from Web_Starbucks.StoreDetailsPage_Web import StoreDetailsPage
from selenium.webdriver.chrome.service import Service
from time import sleep

service_chrome = Service(r"C:\Users\aviva\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.starbucks.com/")

driver.maximize_window()

# Define timeout - In case an element is not found in the program
driver.implicitly_wait(10)


# Instantiate the StarbucksToolBar and StoreLocatorPage classes
starbucks_tool_bar = StarbucksToolBar(driver)
store_locator_page = StoreLocatorPage(driver)
store_details_page = StoreDetailsPage(driver)

# Go to the store locator page
starbucks_tool_bar.go_to_store_locator()

# Search for the store in Prague
store_locator_page.search_store("Prague")

# Select the store information
store_locator_page.select_store_info()

print(store_details_page.get_phone_number().replace(" ", ""))

for i in range(len(store_details_page.opening_hours_rows())):
    print(store_details_page.get_opening_day(i), store_details_page.get_opening_hours(i))


sleep(3)


