def build_user(firstname, lastname, age, *args, **kwargs):
    userInfo = kwargs.copy()
    userInfo['firstname'] = firstname
    userInfo['lastname'] = lastname
    userInfo['age'] = age
    userInfo['others'] = args
    return userInfo

if __name__ == '__main__':
    user = build_user('Tom', 'Hardy', 38, 'male', '1.73cm', job='actor',country='UK')
    print(user)
