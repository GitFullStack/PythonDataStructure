def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    types = [str, list, tuple, set, dict]
    if(start == None):             
        if type(collection) in types:
            if type(collection) != dict:                
                if any(item == sought for item in collection): 
                    print (True)
                else:
                    print(False)                
            else:                             
                if any(value == sought for key, value in collection.items()):                 
                    print (True)
                else:
                    print(False)
                    

    else:
        if(type(collection) in types):
            if(type(collection) != dict and (type(collection) != set)):     
                
                if(type(collection) == list):  
                                        
                    for item in collection[start:]:                   
                        if(sought == item):
                            print(sought)
                        else:
                            print(False)
                elif(type(collection) == str):           
                             
                    if any(string == sought for string in range(start, len(collection))):                           
                        print(True)
                    else:
                        print(False)
                else:
                    if(type(collection) == tuple):     
                                         
                        i = start
                        count = 0
                        while i < len(collection):
                            if (collection[i] == sought):
                                count += 1                            
                            i = i + 1
                        if(count > 0):
                            print(True)
                        else:
                            print(False)
            
            else:
                
                if(type(collection) == dict):                                                              
                    if any(item == sought for item in collection):                 
                        print (True)
                    else:
                        print(False)  
                else:
                    if(type(collection) == set):
                        count = 0
                        for val in collection:
                            if(val == sought):
                                count += 1
                        if(count > 0):
                            print(True)
                        else:
                            print(False)
                


includes({"apple": "red", "berry": "blue"}, "blue")