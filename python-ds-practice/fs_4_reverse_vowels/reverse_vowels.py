def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    vowel_list = []
    strings = list(s)
    org_vowel_dict ={}
    for char in s:
        if(char in vowels):
            vowel_list.append(char)
    
    vowel_list.reverse()  
    for i, item in enumerate(s):
        if(item in vowels):
            org_vowel_dict[i] = item
    c = 0
    while(c < len(vowel_list) ):
        for x in org_vowel_dict.keys():
            org_vowel_dict[x] = vowel_list[c] #Replace vowel in org_vowel_dict with those of vowel_list
            c += 1    
    
    
    for j in org_vowel_dict:        
        strings[j] =  org_vowel_dict[j]    
    my_string = ''.join(strings)
    print(my_string)
    

reverse_vowels("why try, shy fly?")