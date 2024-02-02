def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    for n in word:
        if(letter.lower() == n.lower()):
            count += 1
    print(count)

single_letter_count('EEYuIIIpppppp', 'p')



           
    
