import time

time1 = time.time()
s = ""
for i in range(1000000):
    s += "test"
time2 = time.time()
print("+连接所用时间:"+str(time2 - time1))

time3 = time.time()
t = []
for i in range(1000000):
    t.append("test")
res = "".join(t)
time4 = time.time()
print("join连接所用时间:"+str(time4 - time3))

