"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""

# maybe can use itertools.combinations_with_replacement(iterable, r)
# finding combinations with every possible permutation, including adding to itself

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    # set_nums = set(nums)
    # if 0 in set_nums:
    #     return True
    # do not need the above block of code because python considers -0 == 0)

    set_nums = set(nums)
    for num in set_nums:
        if -num in set_nums:
            return True

    else:
        return False
    # for num in set_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n")
