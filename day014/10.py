with open(r"./test.txt", "r") as f:
    # print(f.read())
    while True:
        s = f.readline()
        print(s, end="")
        if not len(s):
            break