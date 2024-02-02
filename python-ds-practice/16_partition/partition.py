def is_string(el):
    return isinstance(el, str)

def is_even(num):
    return num % 2 == 0

def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    func = fn
    nums = []
    evenNums = []
    oddNums = []
    chars = []
    strs = []
    nonStrs = []
    if(func.__name__ == 'is_even'):
        for i in lst:
            if(func(i)):
                evenNums.append(i)
            else:
                oddNums.append(i)
        nums.append(evenNums)
        nums.append(oddNums)
        print(nums)

    if(func.__name__ == 'is_string'):
        for i in lst:
            if(func(i)):
                strs.append(i)
            else:
                nonStrs.append(i)
        chars.append(strs)
        chars.append(nonStrs)
        print(chars)

partition(["hi", None, 6, "bye"], is_string)
