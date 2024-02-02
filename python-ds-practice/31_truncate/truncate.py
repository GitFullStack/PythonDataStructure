def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    if (n < 3):
        print("Truncation must be at least 3 characters.")
    elif (len(phrase) < n):
        print (phrase)
    else:       
        
        # n - 3 = len(phrase) - x
        # x = len(phrase) - n + 3
        # start = len(phrase) - x
        # start = len(phrase) - (len(phrase) - n + 3)
        # start = len(phrase) - len(phrase) + n - 3
        start = n - 3
        if(len(phrase) >= n):            
            phrase = phrase[:start] + phrase[len(phrase) + 1:]

        phrase += "..."

        print(phrase)

truncate("Hello World", 6)