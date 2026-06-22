from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

GROUP_NAME = "MOWA-Group 5"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print("QR scan karo...")

wait = WebDriverWait(driver,120)

# wait login
search = wait.until(
    EC.presence_of_element_located((By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]'))
)

print("Login ho gaya")

search.click()
search.send_keys(GROUP_NAME)

time.sleep(3)

group = wait.until(
    EC.presence_of_element_located((By.XPATH,f'//span[@title="{GROUP_NAME}"]'))
)

group.click()

time.sleep(4)

# open group info
header = driver.find_element(By.XPATH,'//header')
header.click()

print("Group info open")

# wait members list
members_panel = wait.until(
    EC.presence_of_element_located((By.XPATH,'//div[@role="list"]'))
)

print("Members load ho rahe hain...")

# scroll members
for i in range(400):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", members_panel)
    time.sleep(1)

members = driver.find_elements(By.XPATH,'//span[@title]')

numbers = []

for m in members:
    t = m.get_attribute("title")
    if t and t.replace("+","").isdigit():
        numbers.append(t)

numbers = list(set(numbers))

df = pd.DataFrame(numbers,columns=["Phone"])

df.to_csv("group_members.csv",index=False)

print("Done! CSV file save ho gayi")