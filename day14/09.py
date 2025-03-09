# f = open(r"./test.txt", "w")
# s = "I love Python!"
# f.write(s)
# f.close()

with open(r"./test.txt", "a") as f:
    s = "I learn Python so hard.\n"
    list_text = ["I\n", "am\n", "a\n", "coder!"]
    f.write(s)
    f.writelines(list_text)