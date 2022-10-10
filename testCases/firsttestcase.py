from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utilities.customerLogger import LogGen

serv_object = Service("C:\Automation\Drivers\chromedriver.exe")
logger = LogGen.loggen()

driver = webdriver.Chrome(service=serv_object)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
logger.info('******************firsttestcase execution starts************')
driver.find_element(By.ID, "name").send_keys("alsdfjk")

# driver.close()
