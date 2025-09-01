import json

data = {  "name": "张三", "age": 18, "is_student": True, "money": None }
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

python_dict = json.loads(json_str)
print(python_dict)


data2 = { 'name': '张三', 'age': 18, 'is_student': True, 'money': None, 'hobbies': ['football', 'basketball'] }
with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(data2, f, ensure_ascii=False)

with open('data.json', 'r', encoding='utf-8') as f:
  data3 = json.load(f)
  print(data3)
