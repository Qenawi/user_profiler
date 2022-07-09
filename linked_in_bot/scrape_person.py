import os
from selenium.webdriver.firefox.options import Options
from linkedin_scraper import Person,actions
from selenium import webdriver

options = Options()
options.binary_location = "/home/ahmedqenawi/Downloads/firefox/firefox"

driver = webdriver.Firefox(executable_path="/home/ahmedqenawi/linked_in_profiler/geckodriver" , options= options)
email = os.getenv("ahmu@kl.com")
password = os.getenv("123123")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)
print(person.experiences)
