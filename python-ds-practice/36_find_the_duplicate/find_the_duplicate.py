def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    from iteration_utilities import duplicates
    from iteration_utilities import unique_everseen
    
    dup = list(unique_everseen(duplicates(nums)))
    if(len(dup) > 0):
        if(dup[0] > 0):
            print(dup[0])
    else:        
        print(True)

find_the_duplicate([2, 1, 3, 4]) is None
