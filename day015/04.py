import os


def print_directory(path, level):
    file_list = os.listdir(path)
    for file in file_list:
        file_path = os.path.join(path, file)
        print("\t" * level + file_path[file_path.rfind(os.sep) + 1:])
        if os.path.isdir(file_path):
            print_directory(file_path, level + 1)


print_directory("学习", 0)
