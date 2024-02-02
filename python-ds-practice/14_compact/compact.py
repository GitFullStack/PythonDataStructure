def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [2, 2, 'All done']
    """
    falsy = [[], False, (), None, '', 0.0, 0, 0j, {}, "", range(0), set(), tuple()]
    items = []
    for i in lst:
        if(i not in falsy):
            items.append(i)

    print(items)

compact([0, 1, 2, '', [], False, (), None, 'All done'])
