import traceback

try:
    print("step1")
    num = 1 / 0
except BaseException as e:
    with open("./a.log", "a") as f:
        traceback.print_exc(file=f)
