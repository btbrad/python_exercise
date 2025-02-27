a = [
    ["China", "DeepSeek"],
    ["America", "ChatGPT"],
    ["Europe", "None"]
]

for x in a:
    for y in x:
        print(y, end="\t")
    print("", end="\n")
