from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

geckodriver_path = r"geckodriver.exe"#Enter Geckodriver Location
service = Service(geckodriver_path)

driver = webdriver.Firefox(service=service)
try:
    driver.get("https://www.google.com")
    time.sleep(2) #waiting time to load website
    title = driver.title
    expected_title = "Google"

    if title == expected_title:
        print("Title is correct:", title)
    else:
        print("Title is incorrect. Found:", title)

finally:
    driver.quit()
