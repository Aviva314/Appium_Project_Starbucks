from datetime import datetime

appium_server_url_local = 'http://localhost:4723/wd/hub'
base_url = "https://www.starbucks.com/"

capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    platformVersion="35"
)

starbucks_capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    appActivity='.main.activity.LandingPageActivity',
    appPackage='com.starbucks.mobilecard',
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


def is_store_open(opening_hours):
    current_day = datetime.now().strftime("%A")  # Get current day of the week as a string (e.g., 'Monday')
    current_time = datetime.now().time()  # Get the current time as a `time` object

    for day, period in opening_hours.items():  # Iterate through the opening_hours dictionary
        if current_day == day:  # Check if the current day matches the key in the dictionary
            start_time, end_time = [datetime.strptime(t, "%I:%M %p").time() for t in period.split(" to ")]
            # Convert the 'start_time' and 'end_time' strings to time objects using `datetime.strptime`

            if start_time <= current_time <= end_time:  # Check if the current time is within the store's hours
                return True  # The store is open
    return False  # The store is closed


# Store Example usage
manual_opening_hours = {
    "Monday": "6:30 AM to 9:00 PM",
    "Tuesday": "6:30 AM to 11:00 PM",
    "Wednesday": "6:30 AM to 9:00 PM",
    "Thursday": "6:30 AM to 9:00 AM",
    "Friday": "6:30 AM to 9:00 PM",
    "Saturday": "12:00 AM to 9:00 PM",
    "Sunday": "8:00 AM to 9:00 PM"
}
