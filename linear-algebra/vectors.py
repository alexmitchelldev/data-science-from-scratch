from typing import List

Vector = List[float]

height_weight_age = [
    177, #cm
    68.5, #kg
    31 # years
]
grades = [
    95, # exam1
    80, # exam2
    75, # exam3
    63 # exam4
]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same length!"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1,2,3], [4,5,6]) == [5,7,9]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same length!"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([1,2,3], [4,5,6]) == [-3, -3, -3]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""

    num_vectors = len(vectors[0])
    # Check all vectors are the same size
    assert all([len(vector) == num_vectors for vector in vectors]), "All vectors must be the same length!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_vectors)]

assert vector_sum([[1,2,3], [1,2,3]]) == [2,4,6]

def scalar_multiply(s: float, v: Vector) -> Vector:
    return [el * s for el in v]

assert scalar_multiply(2, [1,2,3]) == [2, 4, 6]

def vector_mean(vectors: List[Vector]) -> Vector:
    num_vectors = len(vectors)

    # return [val / num_vectors for val in vector_sum(vectors)]
    return scalar_multiply(1/num_vectors, vector_sum(vectors))

assert vector_mean([[10, 15, 4], [33, 16, 28]]) == [21.5, 15.5, 16]

print('all tests passed')
