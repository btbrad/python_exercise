def get_extension(filename):
    pos = filename.rfind(".")
    return filename[pos + 1::]

f_name = "text.txt"
print(get_extension(f_name))