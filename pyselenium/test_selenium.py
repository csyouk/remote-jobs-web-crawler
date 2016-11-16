from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.remoteworking.co/#s=2")
print("done!")
sleep(2)
company = driver.find_element_by_class_name("company")
print(company)