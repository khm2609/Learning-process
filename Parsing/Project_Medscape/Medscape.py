import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
from lxml.html import fromstring, tostring
from selenium.common.exceptions import NoSuchElementException
from typing import Union, List
import json


class BioLab:
    agent: WebDriver
    executable_path = r"C:\Users\khvos\OneDrive\Рабочий стол\Analysis\Прога\geckodriver-v0.32.0-win64"

    def __init__(self):
        self.agent = webdriver.Firefox(executable_path=self.executable_path)

    def get_general_info(self) -> dict:
        mainsource = self.agent.find_element(By.XPATH, '//div[@id="maincolboxdrugdbheader"]')
        mainsource = fromstring(mainsource.get_attribute('innerHTML'))

        name = mainsource.xpath('//span[@class="drug_section_link"]/text()')
        comment = mainsource.xpath('//span[@class="drug_suffix"]/text()')
        comment = re.findall(r'\((.*?)\)', str(comment))
        other_names = mainsource.xpath('//span[@class="drugbrandname"]/text()')
        other_names1 = other_names[0].split(',')
        
        other_names_more = mainsource.xpath('//span[@id="drugbrandname_more"]/text()')
        if other_names_more:
            other_names2 = [x for x in other_names1 if x != " "] + other_names_more[0].split(',')
        else:
            other_names2 = [x for x in other_names1 if x != " "]
            
        classes = mainsource.xpath('//a[contains(@href, "https://reference.medscape.com/drugs/")]/text()')
        
        classes1 = []
        for cls in classes:
            if ',' in cls:
                for i in cls.split(','):
                    classes1.append(i.strip())
            else:
                classes1.append(cls.strip())
                
         
        medicine_info = {
        "name": name[0].strip().replace(comment[0],""), 
        "comment": comment[0],
        "other_names": [x.strip() for x in other_names2],
        "classes": classes1,
        "source": None,
        "pregnancy": None,
        "lactation": None
        }

        return medicine_info

    def get_pregnancy_info(self) -> dict:
        commons = self.agent.find_elements(By.XPATH,
        "//div[@id='content_6']/div[@class='refsection_content']/p[following-sibling::h4 or following-sibling:: h3[contains(text(),'Lactation')]]")
        if not commons:
            commons = self.agent.find_elements(By.XPATH,
            "//div[@id='content_6']/div[@class='refsection_content']/p[following-sibling:: h3[contains(text(),'Pregnancy Categories')]]")

        commons_lst = []

        for common in commons:
            common = fromstring(common.get_attribute('innerHTML'))
            common = common.text
            commons_lst.append(common)

        types = self.agent.find_elements(By.XPATH, "//div[@id='content_6']/div[@class='refsection_content']/h4")
        types_lst = []

        for type in types:
            type = fromstring(type.get_attribute('innerHTML'))
            type = type.text
            types_lst.append(type)

        descriptions = self.agent.find_elements(By.XPATH,
        "//div[@id='content_6']/div[@class='refsection_content']//ul[(preceding-sibling::h4) and (following-sibling::h4 or 'Lactation')]")
        descriptions_lst = []
        specifics_lst = []

        for description in descriptions:
            description = fromstring(description.get_attribute('innerHTML'))
            description = description.xpath("//li/text()")
            descriptions_lst.append(description)

        for type in types_lst:
            specifics = {
            "type": type,
            "description": descriptions_lst[int(types_lst.index(type))]
            }
            specifics_lst.append(specifics)

        pregnancy_info = {
            "common": commons_lst,
            "specific": specifics_lst
            }

        return pregnancy_info

        def get_lactation_info(self) -> dict:
            commons = self.agent.find_elements(By.XPATH,
            "//div[@id='content_6']/div[@class='refsection_content']/p[preceding-sibling::h3[text()='Lactation'] and following-sibling::h3[text()='Pregnancy Categories']]")
            if not commons:
                commons = self.agent.find_elements(By.XPATH,
                "//div[@id='content_6']/div[@class='refsection_content']/p[contains(text(), 'Lactation')]")

            commons_lst = []

            for common in commons:
                common = fromstring(common.get_attribute('innerHTML'))
                common = common.text
                commons_lst.append(common)

            lactation_info = {
            "common": commons_lst,
            }
            return lactation_info


    # //div[@id='content_6']/div[@class='refsection_content']/p[contains(text(), "Lactation")]
    # generally) //div[@id='content_6']/div[@class='refsection_content']/p[preceding-sibling::h3[text()='Lactation'] and following-sibling::h3[text()='Pregnancy Categories']]
    # commons = self.agent.find_elements(By.XPATH,
    #                                          "//div[@id='content_6']/div[@class='refsection_content']/p[following-sibling::h4 or following-sibling:: h3]")
    #         commons_lst = []

    def parse(self, med_id: str):
        url = f'{med_id}'
        self.agent.get(url)

        general = self.get_general_info()
        general["source"] = url

        url = f'{med_id}#6'
        self.agent.get(url)

        button = self.agent.find_element(By.XPATH,
                                         '//div[@class="sections-nav"]//li[contains(@class,"li_6 no_subsection")]')
        button.click()

        pregnancy = self.get_pregnancy_info()
        general["pregnancy"] = pregnancy

        lactation = self.get_lactation_info()
        general["lactation"] = lactation
        return general



def save_json(data: Union[List[dict], dict], path: str):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    bio = BioLab()
    res = bio.parse('https://reference.medscape.com/drug/barbidonna-donnatal-belladonna-alkaloids-phenobarbital-999478')
    save_json(res, r"C:\Users\khvos\OneDrive\Рабочий стол\lab2.txt")
