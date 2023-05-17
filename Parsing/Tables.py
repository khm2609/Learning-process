from time import sleep

from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    url = "https://iirmephi.ru/tutorials/npp/datasource_first/"
    driver = webdriver.Firefox(executable_path=r"C:\Users\khvos\OneDrive\Рабочий стол\Прога\geckodriver-v0.32.0-win64\geckodriver.exe")
    driver.get(url)
    source = fromstring(driver.page_source)



    # elements = driver.find_elements(By.XPATH, '//table/thead/tr/th/a')
    # x = [el.text for el in elements]

    elements = source.xpath('//table[contains(@class, "table-striped")]/thead/tr/th/a/text()')
    # print(elements)
    lst = [el.lower() for el in elements]
    print(lst)

    trs = source.xpath('//table[contains(@class, "table-striped")]/tbody/tr')

    for tr in trs:
        row = fromstring(tostring(tr))
        print(row.xpath('//td/text()'))

    # c = {}
    # for i in range(len(trs)): 
    # lines = driver.find_elements(By.XPATH, '//table/tbody/tr')
    # y = [line.text for line in lines]
    # print(y)
    # for i in range(len(y)):
    # yy = driver.find_elements(By.XPATH, '//table/tbody/tr/td[1]')
    # yyy = [l.text for l in yy]
    # print(yyy)
    
