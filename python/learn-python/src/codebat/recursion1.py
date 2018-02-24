def triangle(rows):
    """
    We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks,
    the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of
    blocks in such a triangle with the given number of rows.

    :param rows:
    :return:
    """
    return 0 if rows is 0 else 1 if rows is 1 else rows + triangle(rows - 1)


def fib(n):
    """
    fibonacci math series
    :param n:
    :return:
    """
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


def string_to_int(s):
    """
    convert a string to an int
    :param s:
    :return:
    """
    return _string_to_int(len(s), s)


def _string_to_int(n, s):
    if len(s) == 0:
        return 0
    return n * 10 * int(s[0]) + _string_to_int(n - 1, s[1:])
