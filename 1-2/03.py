import io

s = 'abcdefg'
sio = io.StringIO(s)
sio.seek(3)
sio.write("***")
print(sio.getvalue())