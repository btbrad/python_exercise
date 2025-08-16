'''
找出水仙花数
'''
for num in range(100, 1000):
    low = num % 10
    mid = (num - low) % 100 / 10
    high = (num -low - mid * 10) / 100
    if num == (low ** 3 + mid **3 + high ** 3):
        print(num)    
