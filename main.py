from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import (NoSuchElementException, NoSuchAttributeException, TimeoutException,
                             ElementNotInteractableException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Select what browser is used
service = Service(executable_path="chromedriver.exe")

# Set driver options to determine behaviour

#Initiate driver
driver = webdriver.Chrome(service=service)

# ------------ Input link to automate in path --------------- #
path = ""

driver.get(path)