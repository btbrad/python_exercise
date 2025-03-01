"""
    九九乘法表
"""
for m in range(1, 10):
    for n in range(1, m + 1):
        print(f"{ n } * { m } = { n * m }", end="\t")
    print()