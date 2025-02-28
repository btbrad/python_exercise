a = {"name": "bt", "age": 30, "gender": "male"}
b = dict(name="bt", age=30, gender="male")
c = dict([("name", "bt"), ("age", 30), ("gender", "male")])
print(a)
print(b)
print(c)

d = dict.fromkeys(["name", "age", "gender"])
print(d)

print(a["name"]) #若键不存在，则抛出异常
print(a.get("name")) #若键不存在，则返回None

print(a.items())
print(a.keys())
print(a.values())
print(len(a))
print("name" in a)

a["address"] = "Shanghai"
a["age"] = 18
print(a)

new = {"money": 200, "nickname": "Brad"}
a.update(new)
print(a)

del(a["money"])
print(a)
deleted_element = a.pop("address")
print(deleted_element, a)