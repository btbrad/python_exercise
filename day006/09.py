d1 = {"name": "张三", "age": 18, "salary": 3000, "city": "铁岭"}
d2 = {"name": "李四", "age": 28, "salary": 15100, "city": "合肥"}
d3 = {"name": "王五", "age": 38, "salary": 30000, "city": "上海"}

list_1 = [d1, d2, d3]

for x in list_1:
    if x.get("salary") > 15000:
        print(f"name: { x.get('name') }")