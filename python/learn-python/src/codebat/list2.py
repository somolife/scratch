def big_diff(nums):
    """
    Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

    :param nums:
    :return:
    """
    _min = _max = nums[0]
    for n in nums:
        _min = min(n, _min)
        _max = max(n, _max)

    return _max - _min

