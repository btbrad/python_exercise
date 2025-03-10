import os
import os.path

# os.system("ping www.baidu.com")
print(os.name)
print(os.sep)
print(repr(os.linesep))

print(os.stat("01.py"))

print(os.getcwd())

# os.mkdir("test_os")
# os.rmdir("test_os")

print(os.listdir("../"))

os.chdir("../day014")
print(os.getcwd())

file_list = os.listdir(os.getcwd())
print(file_list)
for file in file_list:
    pos = file.rfind(".")
    extension = file[pos+1:]
    if extension != 'py':
        print(file)

file_list2 = [file for file in file_list if not file.endswith('py')]
print(file_list2)