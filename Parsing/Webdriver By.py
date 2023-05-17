from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__=="__main__":
    url = "https://legalbyte.ru/generator-nazvaniy-firmy-kompanii-brenda-ooo-online-pridumat-nazvanie"
    driver = webdriver.Firefox(executable_path=r"C:\Users\khvos\OneDrive\Рабочий стол\Прога\geckodriver-v0.32.0-win64\geckodriver.exe")
    driver.get(url)

    button = driver.find_element(By.XPATH, '//div[@id="genbtn"]')

    button.click()
    sleep(2)
    elements = driver.find_elements(By.XPATH, '//table/tbody/tr/td[1]/a')
    text = [item.text for item in elements]
    print(text)

    elements = driver.find_elements(By.XPATH, '//table/tbody/tr/td[2]/a')
    text = [item.text for item in elements]
    print(text)
    sleep(2)



    driver.close()

