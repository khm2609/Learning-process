import json
from time import sleep
from typing import List, Union

# from tabulate import tabulate
from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# if __name__ == '__main__':
# url = "https://iirmephi.ru/tutorials/jobhunt/"
# driver = webdriver.Firefox(executable_path=r"C:\Users\мвидео\Desktop\geckodriver.exe")
# driver.get(url)
#
# col_name = ["number","name", "gender"]
# lst=[]
# res = []
# for i in range(1,11):
#     Number = driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/div/table/tbody/tr[{str(i)}]/td[1]')
#     / html / body / div[2] / div[2] / div / table / tbody / tr[1] / td[1]
#     Name = driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/div/table/tbody/tr[{str(i)}]/td[2]')
#     Gender = driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/div/table/tbody/tr[{str(i)}]/td[3]')
#     # data = [f'{Number.text}',f'{Name.text}',f'{Gender.text}']
#     data1 = Number.text
#     data2 = Name.text
#     data3 = Gender.text
#     res.append([data1, data2, data3])
#     k=tabulate(res, headers=col_name, tablefmt="fancy_grid")
# driver.close()
# print(k)
def clicker (driver, x):
    button = driver.find_element(By.XPATH, f'{x}')
    button.click()

def save_json(path: str, data: Union[List[dict], dict]):
    with open(path, "w", encoding="utf-8") as f:
        return json.dump(data, f, indent=4)

def link_data (driver):
    source = fromstring(driver.page_source)
    elementss = source.xpath('//table[contains(@class, "table-striped")]/thead/tr/th/a/text()')
    trs = source.xpath('//table[contains(@class, "table-striped")]/tbody/tr')

    for tr in trs:
        row = fromstring(tostring(tr))
        dct = dict()
        for i, j in zip(elementss, row.xpath('//td/text()')):
            dct[i.lower()] = j

        res.append(dct)

    print(elementss)



if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path=r"C:\Users\khvos\OneDrive\Рабочий стол\Прога\geckodriver-v0.32.0-win64\geckodriver.exe")

    res = []

    for i in range(1, 4):
        url = f"https://iirmephi.ru/tutorials/npp/datasource_first//?page={str(i)}"
        driver.get(url)
        flag = True
        while flag:
            try:
                link_data(driver)
                sleep(3)
                clicker(driver, '/html/body/div[2]/div/div/ul/li[5]/a')
            except NoSuchElementException:
                flag = False
            except Exception as err:
                print(err)
                flag = False

    for i in range(1, 6):
        url = f"https://iirmephi.ru/tutorials/npp/datasource_second//?page={str(i)}"
        driver.get(url)
        flag = True
        while flag:
            try:
                link_data(driver)
                sleep(3)
                clicker(driver, '/html/body/div[2]/div/div/ul/li[7]/a')
            except NoSuchElementException:
                flag = False
            except Exception as err:
                print(err)
                flag = False
    driver.close()
    # res_unique = []
    # for dct in res:
    #     dct.keys

        #     if value
        # y = list(dct.items())[0]
        # if y not in res_unique:
        #     res_unique.append(y)
            # if value not in res.values():
            #     res[key] = value

    save_json(r"C:\Users\khvos\OneDrive\Рабочий стол\nuclear.txt", res)


    print(len(res))
