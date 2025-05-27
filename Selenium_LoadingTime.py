from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

geckodriver_path = r"C:\External\Nanna\Code\sw testing\geckodriver.exe"
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

start = time.time()
driver.get("https://www.google.com")
end = time.time()
print("Page load time:", end - start, "seconds")
driver.quit()