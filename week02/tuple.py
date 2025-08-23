import copy

tp = ()
sp = (32,)
gp = tuple(["its", 30])
my_tuple = (10, 20, 30, 40, 50, 20)
print(my_tuple[2])
print(my_tuple[1:3])
print(my_tuple[:4])
print(my_tuple[3:])
print(my_tuple.count(20))
print(my_tuple.index(20))
newp = copy.deepcopy(my_tuple)
print(newp)

x, y, z = (10, 20, 30)
print(x)
print(y)
print(z)
a, b = (10, 20)
print(a)
print(b)

c, d, *rest = (1, 2, 3, 4, 5)
print(c)
print(d)
print(*rest)
from collections import namedtuple

Point = namedtuple("Point", ("x", "y"))
p = Point(x=1, y=2)
print(p.x)
print(p.y)
print(p[0])
