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