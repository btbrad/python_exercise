dict_hk = {"new": 7, "current": 171}
dict_yn = {"new": 2, "current": 68}
dict_gd = {"new": 1, "current": 40}

# print(dict_hk['current'])
# print(f"{dict_yn['new']}, {dict_yn['current']}")
# dict_gd['new'] += 1
# print(dict_gd['new'])
#
# del dict_hk['current']
# print(dict_hk)
# del dict_gd['new']
# print(dict_gd)
# del dict_yn['new']
# del dict_yn['current']
# print(dict_yn)

for key in dict_hk:
    print(key)
for value in dict_yn.values():
    print(value)
for key, value in dict_gd.items():
    print(key)
    print(value)
for key, value in dict_gd.items():
    if value == 40:
        print(key)
        break

