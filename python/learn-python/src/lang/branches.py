from decorators import print_fn_name


@print_fn_name
def is_positive_fn(n):
    if n > 0:
        print n, "is positive"
    elif n == 0:
        print n, "is zero"
    else:
        print n, "is negative"


@print_fn_name
def raise_error_if_parameter_not_int(p):
    if __debug__:
        if type(p) is not int:
            raise AssertionError("parameter is not int")

    print p, "is all good"


is_positive_fn(10)
is_positive_fn(0)
is_positive_fn(-10)

raise_error_if_parameter_not_int(1)
# raise_error_if_parameter_not_int('a')
