sentence = input("请输入一段英文:")
countDict = {}

for ch in sentence:
    if "A" <= ch <= "Z" or "a" <= ch <= "z":
        countDict[ch] = countDict.get(ch, 0) + 1

for key, value in countDict.items():
    print(f'字母{key}出现了{value}次.')

