def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    str = ''
    for l in phrase:   
        if(to_swap != l):                       #input not equal to current char           
            if(to_swap.lower() == l.lower()):   # lower case input equals lower case current char
                if(to_swap.upper() == l):       # means l is upper case
                    str += l.lower()            # give l opposite case from input
                else:
                    if(to_swap.upper != l):     # means l is lower case
                        str += l.upper()        # give l opposite case from input
            else:                               # means l is not the same character as input
                str += l                        # add current char to str
        else:                                   #input is equal to current char  
            
            if(to_swap.upper() == l):           # means l is upper case
                str += l.lower()                # give l opposite case from input
            else:                               
                if(to_swap.upper != l):         # means l is lower case
                    str += l.upper()            # give l opposite case from input     
    print(str)

flip_case('Aaaahhh', 'h')
