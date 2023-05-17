import json
import os
from typing import List, Union


def read_json(path: str) -> Union[dict, list]:
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def safe_json(path: str, data: Union[List[dict], dict]):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    # f = read_json(r"C:\Users\khvos\OneDrive\Рабочий стол\biodata\S014296122030627X.json")
    # print(f)
    # print(f["title"])
    # print(f["keywords"])
    main_dir = r"C:\Users\khvos\OneDrive\Рабочий стол\biodata"
    files_name = os.listdir(main_dir)
    # print(files_name)
    keywords_list = []
    for name in files_name:
        fullpath = f"{main_dir}/{name}"
        data = read_json(fullpath)
        keywords = data["keywords"]
        for k in keywords:
            keywords_list.append(k)
    # print(keywords_list)
    result = {}
    for keyword in keywords_list:
        stat = keywords_list.count(keyword)
        result[keyword] = stat
    print(result)

    safe_json(r"C:\Users\khvos\OneDrive\Рабочий стол\tmp.json", result)
    

    # print(frequency)
# сохрание данных в файл джейсон top 10 keywords
