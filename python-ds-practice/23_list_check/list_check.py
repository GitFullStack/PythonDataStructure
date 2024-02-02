def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    is_list = [True if type(i) == list else False for i in lst]
   
    print(all(is_list))

list_check([[1], "nope"])
