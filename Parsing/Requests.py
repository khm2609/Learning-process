import requests

if __name__ == "__main__":
    url = "https://legalbyte.ru/generator-nazvaniy-firmy-kompanii-brenda-ooo-online-pridumat-nazvanie"

    driver = webdriver.Firefox()
    driver.get(url)

    
    req = requests.get(url)

    print(req.text)
    #$x("//div[@id='genbtn']")