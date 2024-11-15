def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row from the triangle
        # Create the new row by adding pairs of adjacent elements
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
