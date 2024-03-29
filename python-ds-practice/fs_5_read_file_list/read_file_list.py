def read_file_list(filename):
    
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    import os
    path = os.path.join('C:/Users/souri/OneDrive/Desktop/SpringBoard/Python/python-ds-practice/python-ds-practice/fs_5_read_file_list/', filename + '.' + 'txt')
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    
    # Strips the newline character
    for line in Lines:
        print("- {}".format( line.strip()))
    file1.close()

read_file_list('dogs')