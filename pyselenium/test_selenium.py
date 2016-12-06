from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.remoteworking.co/#s=2")
print("done!")
sleep(5)
company = driver.find_element_by_class_name("company")
print "company : ", company

companies = driver.find_elements_by_tag_name("a")
for company in companies:
    print "text : ", company.text
# print "companies", companies
print dir(companies[0])
