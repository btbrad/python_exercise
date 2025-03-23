def test():
    print('start')
    i = 0
    while i < 3:
        yield i
        print(f'i: { i }')
        i += 1
    print('end')
    return 'done'


if __name__ == '__main__':
    a = test()
    print(a)
    a.__next__()
    a.__next__()
    a.__next__()
    a.__next__()
