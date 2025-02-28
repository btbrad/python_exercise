d1 = {"name": "张三", "age": 20, "money": 100}
d2 = {"name": "李四", "age": 28, "money": 500}
d3 = {"name": "王五", "age": 16, "money": 800}

l = [d1, d2, d3]
print(l)
print(l[2].get("age"))

for m in range(len(l)):
    for n in l[m].keys():
        print(l[m].get(n), end="\t")
    print("", end="\n")
