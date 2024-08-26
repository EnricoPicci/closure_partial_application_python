# Description: Multiply two matrices using list comprehension
# Example taken from https://www.programiz.com/python-programming/examples/multiply-matrix
def mult_matrices_list_comprehension(
    matrix_1: list[list[float]], matrix_2: list[list[float]]
) -> list[list[float]]:
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_2)]
        for row in matrix_1
    ]


def mult_matrices_curried(matrix_1: list[list[float]]):
    def inner(matrix_2: list[list[float]]) -> list[list[float]]:
        return mult_matrices_list_comprehension(matrix_1, matrix_2)

    return inner


if __name__ == "__main__":
    matrix_1 = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    # Output: [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
    matrix_2 = [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
    # Output: [[27, 30, 33], [61, 68, 75], [95, 106, 117]]

    prod = mult_matrices_list_comprehension(matrix_1, matrix_2)
    prod_curried = mult_matrices_curried(matrix_1)(matrix_2)

    print(f"Matrix product using list comprehension:")
    print(prod)
    print(f"\nMatrix product using currying:")
    print(prod_curried)

    print("\nAre the 2 matrices equal?")
    print(prod == prod_curried)


# python -m currying.mult_matrices
