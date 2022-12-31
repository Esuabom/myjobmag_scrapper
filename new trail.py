from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="C:/Program  Files (x86)/chromedriver_win32/chromedriver.exe", options=options)
driver.get("https://www.reed.co.uk/jobs/visa-sponsorship-jobs")
time.sleep(5)
element_no = 1
for i in range(5):
    print("I.m here now")
    list_of_jobs = driver.find_elements(By.XPATH, "//*/h2/a")
    list_of_jobs[element_no].click()
    time.sleep(5)
    print("2nd step")
    output = driver.find_element(By.XPATH, '//div[@class="col-xs-12"]/h1').text
    print(output)
    print("3rd step")
    driver.back()
    time.sleep(2)
    print("final")
    element_no += 1
    


