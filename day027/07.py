def double(arg):
    print('before: ', arg)
    arg = arg * 2
    print('after: ', arg)

def change(arg):
    print('before: ', arg)
    arg.append('More Data')
    print('after: ', arg)

num = 10
double(num)
print(num)

l = [1, 2, 3]
change(l)
print(l)