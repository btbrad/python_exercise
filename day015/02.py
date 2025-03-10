import os

path = os.getcwd()

file_list = os.walk(path, topdown=True)

for root,dirs,files in file_list:
    for name in dirs:
        print(os.path.join(root, name))
    for name in files:
        print(os.path.join(root, name))
