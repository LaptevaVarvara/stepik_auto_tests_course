#Задание: ждем нужный текст на странице 2.4.8
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button1 = browser.find_element(By.CSS_SELECTOR, "[onclick='checkPrice();']")
button1.click()

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = calc(x_element.text)

input1 = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(x)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)
