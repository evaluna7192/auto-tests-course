from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Petrov")
	
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivan")
	
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@gmail.com")
	 

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'new.txt')           # добавляем к этому пути имя файла 
    file1 = browser.find_element_by_css_selector("[type = 'file']")
    file1.send_keys(file_path)
	
	

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
