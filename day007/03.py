names = ("张三", "李四", "王五", "刘六")
ages = (18, 20, 16)
genders = ("male", "female")

for name, age, gender in zip(names, ages, genders):
    print(f"{ name }--{ age }--{ gender }")