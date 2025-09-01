def outer():
  a = [1, 2, 3]
  def inner(x):
    a.append(x)
    print(a)
  return inner

fun1 = outer()
fun2 = outer()
fun1(4)
fun1(4)
fun2(4)