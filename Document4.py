from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
  return x + y

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	
    x_element= browser.find_element_by_id("num1")
    y_element= browser.find_element_by_id("num2")
    x = x_element.text
    y = y_element.text
    print (x)
    print (y)
    x = int(x)
    y = int(y)
    z = calc(x,y)
    z = str(z)
    print(z)
	

    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
