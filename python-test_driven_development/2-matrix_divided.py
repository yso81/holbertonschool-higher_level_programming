#!/usr/bin/python3
"""
    function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    All elements of the matrix should be divided by div

    Args:
    matrix (list of lists): A matrix (list of lists) of integers or floats
    div (int or float): The number to divide by

    Raises:
    TypeError: if matrix is not a matrix (list of lists) of integers/floats
    TypeError: if Each row of the matrix is not the same size
    TypeError: if div is not a number
    ZeroDivisionError: if division by zero

    returns:
    A new matrix with all elements divided by div,
    rounded to 2 decimal places
    """
    if not isinstance(matrix, list):
        if not (isinstance(row, list) for row in matrix):
            raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    if not matrix:
        return []
    
    row_length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/2-matrix_divided.txt", verbose = True)


