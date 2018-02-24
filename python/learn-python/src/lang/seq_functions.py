"""
useful for functional programming style
"""
from decorators import print_fn_name


@print_fn_name
def seq_as_sorted_set(_seq):
    for f in sorted(set(_seq)):
        print f


@print_fn_name
def seq_reverse(_seq):
    for i in reversed(_seq):
        print i


seq_as_sorted_set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
seq_reverse(xrange(1, 10, 2))

# functional
print "filter:", filter(lambda x: x < 5, xrange(1, 10, 2))
print "map:", map(lambda x: (x, x * x), filter(lambda x: x > 1, xrange(1, 5, 1)))
print "reduce:", reduce(lambda x, y: x + y, filter(lambda x: x > 1, xrange(1, 5, 1)))
print "list comprehension x^2:", [x ** 2 for x in range(2, 10, 2)]
print "list comprehension div2_3:", [x for x in range(1, 30) if x % 2 == 0 and x % 3 == 0]

list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

list = [[]] * 5
print list  # a list of 5 lists, however they all reference the same list
list[0].append(10)
print list  # output?
list[1].append(20)
print list  # output?
list.append(30)
print list  # output?
