m1 = [
            [1,   2],
            [30, 40],
     ]         

m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diagonal1 = 0
    diagonal2 = 0    
    c1 = 1    
    list_count = len(matrix)    
    item_count = len(matrix[c1-1])
    while (c1 <= list_count): # while less than or equal last list
            diagonal1 += matrix[c1-1][c1-1]
            diagonal2 += matrix[c1-1][item_count-1]
            c1 += 1
            item_count = item_count - 1
            
    print(diagonal1 + diagonal2)

sum_up_diagonals(m2)