'''
练习：将下列英文语句按照单词进行翻转.
转换前：To have a government that is of people by people for people
转换后：people for people by people of is that government a have To
'''
p = 'To have a government that is of people by people for people'
# new_p = '_'.join(p)
# print(new_p)
new_list = p.split(' ')
reversed_str = ''
for i in range(len(new_list)-1, -1, -1):
    reversed_str += new_list[i] + ' '

print(reversed_str)