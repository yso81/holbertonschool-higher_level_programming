#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows

    Args:
        n (int): The number of rows for Pascal's triangle

    Returns:
        list: A list of lists of integers representing Pascal's triangle
              Returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j+1])
            row.append(1)
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))