import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Excel file read
data = pd.read_excel("numbers.xlsx")

# Message to send
message = "Assalamualaikum! Ye automated message hai."

# Chrome driver setup
driver = webdriver.Chrome()  # chromedriver.exe must be in same folder
driver.get("https://web.whatsapp.com")

print("QR code scan karo aur WhatsApp Web open karo...")
time.sleep(20)  # time to scan QR code

for number in data["phone"]:
    try:
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(url)

        # Wait for input box to load
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            )
        )

        # Send message using Enter key
        input_box.send_keys(Keys.ENTER)

        print("Message sent to:", number)

    except Exception as e:
        print("Failed to send to:", number, "| Error:", e)

    # Delay before next number
    time.sleep(10)

print("All done! Script finished.")