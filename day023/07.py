phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

list1 = plist[1:8]
list1.remove("'")
list1.remove(" ")
list1.insert(3, list1.pop())
list1.insert(2, ' ')
plist = list1.copy()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
