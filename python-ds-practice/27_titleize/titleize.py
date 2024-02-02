def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = [i for i in phrase.split()]
    new_phrase = ''
    for i in words:
        new_phrase += i.capitalize() + ' '
    print(f"'{new_phrase.strip()}'")

titleize('oNLy cAPITALIZe fIRSt')