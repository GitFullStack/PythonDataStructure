def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    from collections import Counter
    mismatch = 0
    count1 = Counter(str(num1))
    count2 = Counter(str(num2))
    for n1 in count1:
        for n2 in count2:
            if (str(num1).count(n1, 0) == str(num2).count(n2, 0)):
              mismatch = 0  
            else:  
                mismatch =+ 1              
                break

    if(mismatch == 0):
        print(True)
    else:
        print(False)

same_frequency(1212, 2211)