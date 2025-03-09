def is_triangle(a, b, c):
    return (a + b > c) or (a + c > b) or (b + c > a)

print(is_triangle(1, 2, 3))
print(is_triangle(b = 2, c = 3, a = 4))