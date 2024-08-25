'''
定义函数,根据总两数,计算几斤零几两.:
total_liang = int(input("请输入两:"))
jin = total_liang // 16
liang = total_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")
'''

def calc_jin():
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")

calc_jin()