print("May Had a little lamb.")
print("It's fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

print("{} {}".format('Hello', 'World'))
print('{1} {0} {1}'.format('Hello', 'World'))
print('网站名：{name}, 地址： {url}'.format(name='百度', url='www.baidu.com'))

site = {'name': '百度', 'url': 'www.baidu.com'}
print('网站名：{name}, 地址： {url}'.format(**site))

my_list = ['百度', 'www.baidu.com']
print('网站名：{0[0]}, 地址：{0[1]}'.format(my_list))