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

def vector_sum(vectors: List[Vector]):
    """Sums all vectors"""
    assert all([len(vector) == len(vectors[0]) for vector in vectors]), "All vectors must be the same length!"

    return None

vector_sum([height_weight_age, height_weight_age])
print('all tests passed')
