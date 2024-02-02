def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    string = ''
    n = 0
    
    if(type(num) == int and num >= 0):
        if(num > 0):
            while( num - 1 >= 0 ):
                num = num - 1
                string += phrase            
            print (string)
        else:
            if(num == 0):
             print ('')
    else:
        print (None)


repeat('abc', 1)
