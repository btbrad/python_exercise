status = 404

match status:
    case 200:
        print('成功')
    case 304:
        print('重定向')
    case 404:
        print('未找到')
    case _:
        print('不合法的状态码')