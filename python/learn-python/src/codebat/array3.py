def max_span(nums):
    """
    Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is
    the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span
    found in the given array. (Efficiency is not a priority.)

    :param nums:
    :return:
    """
    d = dict()
    for i, v in enumerate(nums):
        if v not in d:
            d[v] = (i, i)
        else:
            d[v] = (d[v][0], i)
    m = 1
    for k, v in d.items():
        m = max(v[1] - v[0] + 1, m)
    return m
