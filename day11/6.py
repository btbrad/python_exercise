'''
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
1. 打印所有商品信息,
 格式：商品编号xx,商品名称xx,商品单价xx.
2. 打印所有订单中的信息,
格式：商品编号xx,购买数量xx.
3. 打印所有订单中的商品信息,
格式：商品名称xx,商品单价:xx,数量xx.
4. 查找数量最多的订单(使用自定义算法,不使用内置函数)
5. 根据购买数量对订单列表降序(大->小)排列
'''

# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# for x in dict_commodity_infos:
#     print("商品编号%d,商品名称%s,商品单价%d." % (x, dict_commodity_infos[x]["name"], dict_commodity_infos[x]["price"]))

# for x in list_orders:
#     print("商品编号%d,购买数量%d." % (x["cid"], x["count"]))

# for x in list_orders:
    # info = dict_commodity_infos[x["cid"]]
    # print("商品名称%s,商品单价:%d,数量%d." % (info["name"], info["price"], x["count"]))

# max_c = 0
# max_order = {}
# for x in list_orders:
#     if max_c < x["count"]:
#         max_c = x['count']
#         max_order = x
#
# print(max_order)

for x in range(len(list_orders) -1):
    for y in range(len(list_orders) - x - 1):
        if list_orders[y]["count"] < list_orders[y+1]["count"]:
            list_orders[y], list_orders[y+1] = list_orders[y+1], list_orders[y]

print(list_orders)