from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

service = Service(r"geckodriver.exe")#Enter Geckodriver Location
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

print("Search completed")
driver.quit()
