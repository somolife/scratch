def group_sum(start, nums, target):
    """
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the
    given target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking
    strategy in this problem, you can use the same pattern for many problems to search a space of choices.
    Rather than looking at the whole array, our convention is to consider the part of the array starting at
    index start and continuing to the end of the array. The caller can specify the whole array simply by passing
    start as 0. No loops are needed -- the recursive calls progress down the array.
    
    :param start: 
    :param nums: 
    :param target: 
    :return: 
    """
    if target is 0:
        return True
    if start == len(nums):
        return False
    return target == nums[start] or \
           group_sum(start + 1, nums, target - nums[start]) or \
           group_sum(start + 1, nums, target)


def split_array(nums):
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sums of the two groups
    are the same. Every int must be in one group or the other. Write a recursive helper method that takes whatever 
    arguments you like, and make the initial call to your recursive helper from splitArray(). (No loops needed.)

    :param nums: 
    :return: 
    """
    if len(nums) == 0:
        return True
    l1 = []
    l2 = []
    l2.extend(nums)
    return _split_array(0, l1, l2, 0)


def _split_array(level, l1, l2, val):
    if len(l2) <= 0:
        return False
    if _net_sum(l1, l2, val):
        return True

    for n in l2:
        l1.append(l2.pop(0))
        if _split_array(level + 1, l1, l2, val):
            return True
        l2.append(l1.pop(level))


def _net_sum(l1, l2, val):
    _sum = 0
    for n in l1:
        _sum += n
    for n in l2:
        _sum -= n
    return val == _sum
