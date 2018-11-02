import math

"""vector addition"""
def vector_add(v, w):
    return [v_i+w_i for v_i,w_i in zip(v,w)]

"""vector subtraction"""
def vector_subtract(v, w):
    return [v_i-w_i for v_i,w_i in zip(v,w)]

"""vector summation"""
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

"""Alternative method for vector summation"""
from functools import partial,reduce
vector_sum = partial(reduce, vector_add)

"""vector scaling"""
def scalar_multiply(c,v):
    return [c*v_i for v_i in v]

"""vector mean"""
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

"""dot product"""
def dot(v,w):
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    """(v_1 - w_1) ** 2 + ... + (v_n -w_n) **2"""
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return magnitude(vector_subtract(v,w))

