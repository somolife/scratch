from decorators import print_fn_name


@print_fn_name
def for_over_number_range(n):
    for i in range(0, n):
        print i


@print_fn_name
def for_over_number_range_countdown(n):
    for i in range(n, 0, -1):
        print i


@print_fn_name
def for_over_list(_list=[]):
    for item in _list:
        print item


@print_fn_name
def for_over_list_enumerate(_list=[]):
    for i, item in enumerate(_list):
        print i, "-->", item


@print_fn_name
def for_over_dict(_dict={}):
    for key, value in _dict.iteritems():
        print key, value


@print_fn_name
def for_over_tuple(_tuple=[]):
    for v1, v2 in _tuple:
        print v1, v2


@print_fn_name
def while_over_number_range(n):
    i = 0
    while i < n:
        print i
        i += 1


@print_fn_name
def break_and_continue():
    x = 5
    while x > 0:
        print x
        break
        x -= 1
        print x

    l = [5, 6, 7]
    for x in l:
        continue
        print x  # never reaches this line


for_over_number_range(3)
for_over_number_range_countdown(3)
for_over_list(['a', 'b', 'c'])
for_over_list_enumerate(['a', 'b', 'c'])
for_over_dict({'a': 100, 'b': 200})
for_over_tuple([(1, 1), (2, 4), (3, 9)])
while_over_number_range(3)
break_and_continue()
