'''
八大行星："水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星"
 -- 创建列表存储4个行星：“水星” "金星" "火星" "木星"
 -- 插入"地球"、追加"土星" "天王星" "海王星"
 -- 打印距离太阳最近、最远的行星(第一个和最后一个元素)
 -- 打印太阳到地球之间的行星(前两个行星)
 -- 删除"海王星",删除第四个行星
 -- 倒序打印所有行星(一行一个)
'''
star_list = ['水星', '金星', '火星', '木星']
star_list.insert(2, '地球')
star_list.append('土星')
star_list.append('天王星')
star_list.append('海王星')
print(star_list)
print(f'距离太阳最近:{star_list[0]}')
print(f'距离太阳最远:{star_list[-1]}')
print(f'太阳到地球之间的行星:{star_list[0:2]}')
star_list.remove('海王星')
del star_list[3]
print(star_list)
for star in star_list[::-1]:
    print(star)
for i in range(len(star_list) - 1, -1, -1):
    print(star_list[i])
