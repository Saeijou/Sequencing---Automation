import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

WAIT_TIME = 5

# Prepare the Automation Framework
ser = Service(r"C:\\Users\steph\PycharmProjects\chromedriver.exe")

op = webdriver.ChromeOptions()
op.add_argument("--window-size=1080,1080")
driver = webdriver.Chrome(service=ser, options=op)

# Fetch Website
driver.get("https://computer-database.gatling.io")
time.sleep(WAIT_TIME)

# Search for "a" in the Searchfield using the "Filter by name" button
search = driver.find_element(By.ID, "searchbox")
search.clear()
search.send_keys("a")
apply_button = driver.find_element(By.ID, "searchsubmit")
apply_button.click()

time.sleep(WAIT_TIME/2)

# Click "next" button
#next_button = driver.find_element(By.XPATH, "/html/body/section/div[2]/ul/li[3]/a")
next_button = driver.find_element(By.LINK_TEXT, "Next →")
next_button.click()
time.sleep(WAIT_TIME / 4)

# Click "previous" button
prev_button = driver.find_element(By.LINK_TEXT, "← Previous")
prev_button.click()
time.sleep(WAIT_TIME/2)

# Click "Add a new computer"
add_button = driver.find_element(By.ID, "add")
add_button.click()
time.sleep(WAIT_TIME / 5)

# Add variables
name = driver.find_element(By.ID, "name")
name.send_keys("Skynet")
time.sleep(WAIT_TIME / 5)

introduced = driver.find_element(By.ID, "introduced")
introduced.send_keys("1984-01-01")
time.sleep(WAIT_TIME / 5)

discontinued = driver.find_element(By.ID, "discontinued")
discontinued.send_keys("2019-01-01")
time.sleep(WAIT_TIME / 5)

company = driver.find_element(By.ID, "company")
company.send_keys("Atari")
time.sleep(WAIT_TIME / 5)

create_button = driver.find_element(By.CSS_SELECTOR, ".btn")
create_button.click()

time.sleep(WAIT_TIME)

# Verify the success message
success_message = driver.find_element(By.CSS_SELECTOR, ".alert-message")
print(success_message.text)

time.sleep(WAIT_TIME)

# Search for "Skynet" in the Searchfield clicking "Enter" to search
search = driver.find_element("id", "searchbox")
search.send_keys("Skynet")
search.send_keys(Keys.ENTER)
