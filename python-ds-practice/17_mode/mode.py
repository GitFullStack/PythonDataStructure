def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    l_key = None
    numCounts = {}
    unique_nums = list(set(nums))
    for num in unique_nums:
        numCounts[num] = nums.count(num)
    l_key = max(numCounts, key=numCounts.get)
    print(l_key)
    

mode([2, 2, 3, 3, 2])
