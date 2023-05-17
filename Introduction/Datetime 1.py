from datetime import datetime, timedelta

import requests

# def safe_json(path: str, data: Union[List[dict], dict]):
#     with open(path, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4)

if __name__ =="__main__":
    # for code in ['ru', 'es', 'at', 'us', 'fr', 'ch', 'cn', 'af', 'ua']:
        url = f'https://corona-api.com/countries/us'
        res = requests.get(url)
        data = res.json()
        # print(data['data']['timeline'])
        items = data['data']['timeline']
        print(items)
        s = 0
        k = 0
        for item in items:
            date = datetime.strptime(item['date'],'%Y-%m-%d')
            value = item['new_deaths']
            if date <= datetime.today() - timedelta(days=30):
                break
            else:
                s += value
                k += 1
        print(s/k)
    # safe_json(r"C:\Users\khvos\OneDrive\Рабочий стол\tmp.json", code, s/k)