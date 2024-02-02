def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    leng = len(phrase)
    midpoint = None 
    forward = ''
    backward = ''
    
    if(int(leng%2)==0):
        midpoint = int(leng/2)
        #range(start, stop, step)
        for i in range(0, midpoint, 1):
            forward += phrase[i]        
        
        for i in range(leng - 1, midpoint - 1, -1):
            backward += phrase[i]           
            
    else:
        midpoint = int(leng/2)
        for i in range(0, midpoint, 1):
            forward += phrase[i]        
        
        for i in range(leng - 1, midpoint, -1):
            backward += phrase[i]  
    if(forward.lower() == backward.lower()):
        print(True)
    else:
        print(False)

is_palindrome('byba')
