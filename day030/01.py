name = '张三'
age = 20

print(f'姓名：{name=}， 年龄：{age}')

score = '及格'
print(f'{score:*^20}')

price = 2.5
print(f'{price=:.2f}')

info = 'btbrad'
print(info.removeprefix('bt'))
print(info.removesuffix('brad'))

def new_func(num: int | float)-> int|float:
    return num * 2

print(new_func(2))

value = 4
print(bin(4).count('1'))
print(value.bit_count())