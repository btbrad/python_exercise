text = """我是一个程序员，我正在学习python基础，希望以后做一个
    全栈开发人员"""

print(len(text))
print(text.startswith("我"))
print(text.endswith("人员"))
print(text.find("一"))
print(text.rfind("一"))
print(text.count("员"))
print(text.isalnum())


s1 = "aabbcc"
s2 = "aabbcc"
print(s1 is s2)
print(s1 == s2)
