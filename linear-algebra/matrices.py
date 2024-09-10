from typing import Tuple, Sequence, Callable

Matrix = Sequence[Sequence[float]]

height_weight_age = [
	[178, 68, 31],
	[160, 52, 30],
	[190, 100, 39]
]

def shape(A: Matrix) -> Tuple:
    n = len(A)
    k = len(A[0])

    return (n, k)

assert shape(height_weight_age) == (3, 3)

def get_row(A: Matrix, i: int) -> Sequence[float]:
    return A[i]

assert get_row(height_weight_age, 1) == height_weight_age[1]

def get_column(A: Matrix, j: int) -> Sequence[float]:
    return [n[j] for n in A]

assert get_column(height_weight_age, 1) == [68, 52, 100]

def make_matrix(n: int, callback: Callable[[int, int], float]) -> Matrix:
    return  [[callback(i, j) for j in range(n)] for i in range(n)]

identity_matrix = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

assert make_matrix(5, lambda i, j: 1 if i == j else 0) == identity_matrix

heavier_than = [
    [0, 1, 0],
	[0, 0, 0],
	[1, 1, 0]
]

def make_relationship_matrix(A: Matrix, k: int) -> Matrix:
    def compare(j, n) -> float:
        return 1 if A[n][k] > A[j][k] else 0

    return [[compare(j, n) for j in range(len(A[0]))] for n in range(len(A))]

assert make_relationship_matrix(height_weight_age, 1) == heavier_than
