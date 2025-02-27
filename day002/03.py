import io

s = 'abcdefg'
sio = io.StringIO(s) #可变字符串
sio.seek(3) #指针索引到3
sio.write("***")
print(sio.getvalue())