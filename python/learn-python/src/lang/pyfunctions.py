"""
is python pass by value, reference?

"""


class P:
    n = 10


def m1(n):
    n += 1
    return n


def m2(p):
    p.n = 20
    p = P
    return p


def extendList(val, list=[]):
    list.append(val)
    return list


def multipliers_buggy():
    return [lambda x: i * x for i in range(4)]


def multipliers():
    for i in range(4): yield lambda x: i * x


# pass by value for primitives
x = 5
m1(x)
print x

# pass by value for objects
y = P
m2(y)
print y.n

# default arguments are evaluated once, upon function definition
list1 = extendList(10)
print "list1 = %s" % list1
list2 = extendList(123, [])
print "list2 = %s" % list2
list3 = extendList('a')
print "list3 = %s" % list3  # reused list1

# closures are late-binding
print [m(2) for m in multipliers_buggy()]
print [m(2) for m in multipliers()]
