def outer():
    print('outer')
    a = 3

    def inner():
        print('inner')
        nonlocal a
        a = 4
        print(f'a: {a}')

    return inner

fn = outer()
fn()