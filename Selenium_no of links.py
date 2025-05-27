from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

geckodriver_path = r"geckodriver.exe"#Enter Geckodriver Location
service = Service(geckodriver_path)

driver = webdriver.Firefox(service=service)

try:
    driver.get("https://www.google.co.in")
    links = driver.find_elements(By.TAG_NAME, "a")
    print("Total No. of Links:", len(links))

finally:
    driver.quit()
