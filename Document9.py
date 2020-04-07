from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
	
    x_element= browser.find_element_by_id("input_value")
    x = x_element.text
    print (x)
    y = calc(x)
	
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
	
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
