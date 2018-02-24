from collections import Set, Mapping, deque
from numbers import Number

from sys import getsizeof

from decorators import print_fn_name

zero_depth_bases = (basestring, Number, xrange, bytearray)
iteritems = 'iteritems'


@print_fn_name
def print_class(args=[]):
    for i in args:
        print repr(i), "-->", type(i).__name__, "[ size:", getsize(i), "]"


def getsize(obj):
    """
    Recursively iterate to sum size of object & members in bytes
    :param obj:
    :return:
    """

    def inner(obj, _seen_ids=set()):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size =getsizeof(obj)
        if isinstance(obj, zero_depth_bases):
            pass  # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, iteritems):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, iteritems)())
        # Now assume custom object instances
        elif hasattr(obj, '__slots__'):
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        else:
            attr = getattr(obj, '__dict__', None)
            if attr is not None:
                size += inner(attr)
        return size

    return inner(obj)


print_class([print_class, 1, 1.0, -1, 'a', "string", [1, 2], (3, 4, 5), {'a': 1, 'b': 2}])
