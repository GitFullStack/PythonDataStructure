def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
        num2 = nums
    count = 0
    for ind1, v1 in enumerate(nums):        
        for ind2, v2 in enumerate(num2): 
            if(ind1 != ind2 and (v1 + v2 == goal)):                
                print((v1, v2))    
                count += 1                            
                nums.pop(0)                                           
                num2.pop(0)
    if(count == 0 ):
        print (())

                
                
             

sum_pairs([11, 20, 4, 2, 1, 5], 100)
