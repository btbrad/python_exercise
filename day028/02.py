def test():
    print('start')
    i = 0
    while i < 3:
        temp = yield i
        print(f'temp: {temp}')
        i += 1
    print('end')
    return 'done'


if __name__ == '__main__':
    g = test()
    print(next(g))
    print(g.send(100))
    print(next(g))