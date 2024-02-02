lst = [1, 2, 3, 4, 5]

def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    new_lst = [] 

    i = 0
    new_list = []
    for l in lst:        
        if (i % 2 == 0):
            new_list.append(l)
        i += 1 
    print(new_list)
    

remove_every_other(lst)