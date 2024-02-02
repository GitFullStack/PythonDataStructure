def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    left_count = parens.count('(')
    right_count = parens.count(')')
    i = 0
    if(left_count == right_count and (parens[0]!=')' and parens[len(parens)-1 !='('])):
        left_count = 0 #resetting left_count
        right_count = 0 #resetting right_count        
        while(i < len(parens) - 1):  
            if(i<=1):     
                left_count += 1 #If we are here it means the first char is (
                if(parens[i + 1] == ')'):
                    left_count = left_count - 1                        
                else:
                    left_count +=  1    
            else:
                if(parens[i] == '('):                
                    left_count += 1
                    if(parens[i + 1] == ')'):
                        left_count = left_count - 1                        
                    else:
                        left_count +=  1                        
                elif(parens[i] == ')'): #if value of index 3 is right paren
                    right_count +=1
                    if(parens[i-1] == '('):
                        left_count = left_count - 1
                        right_count = right_count -1
                    
                    if (parens[i+1] == ')'):
                            right_count += 1
                    else:
                        left_count += 1
            i += 2   
    else:
        if(parens[0]==')'):
              left_count = 0
              right_count = 0
              right_count +=  1
        else:
            if (parens[len(parens)-1 =='(']):
                left_count = 0
                right_count = 0
                left_count += 1        

    if(left_count == right_count):
        print(True)
    else:
        print(False)
    
valid_parentheses("((()))")