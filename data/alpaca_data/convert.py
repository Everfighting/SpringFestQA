import csv
import json

csv_file_path = './data/bg5.csv'  # 替换为CSV文件的路径
convert_json = './data/bg5.json'

json_data = []

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        question = row['question']
        answer = row['answer']
        alpaca_json = {
            'instruction': question,
            'input':'',
            'output': answer,
        }
        json_data.append(alpaca_json)

# 将JSON数据写入文件

with open(convert_json, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)