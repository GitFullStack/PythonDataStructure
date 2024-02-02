def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    total = None
    for i in range(0, len(nums), 1):
        if((i == 0 and nums[i] % 2 == 0) or (i == 1 and nums[i] % 2 == 0)):            
            total = nums[i]
          
        elif (nums[i] % 2 == 0):
            total *= nums[i]
           

    if(total == None):
        print(1)

    else:
        print(total)

multiply_even_numbers([1, 3, 5])