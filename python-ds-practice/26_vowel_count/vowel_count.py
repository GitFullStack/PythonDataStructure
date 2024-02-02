def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ["a", "e", "i", "o", "u"]
    vowels_occ = {}
    new_phrase = phrase.lower()
    for c in new_phrase:   
        if(c in vowels):           
           vowels_occ[c] = new_phrase.count(c)

    print(vowels_occ)

vowel_count('rithm school') 
