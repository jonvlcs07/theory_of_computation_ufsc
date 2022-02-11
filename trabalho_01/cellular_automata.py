'''
Trabalho 01 Teoria da Computação


Wish_list:
    - Cellular automata (Class):
        - Init
        - Sum d closest elements
        - Next automata.

    - Circular array data structure (Class)
        - Cicular distance
        - Get elements at distance d


'''


# %% Tests and definitions
import numpy as np


test_01 = '''5 3 1 1\n1 2 2 1 2'''

expected_01 = '''2 2 2 2 1'''

test_02 = '''5 3 1 10\n1 2 2 1 2'''

expected_02 = '''2 0 0 2 2'''

print('Teste 01')
print(test_01)

print('Valor esperado de saída:')
print(expected_01)

print('\nTeste 02')
print(test_02)

print('Valor esperado de saída:')
print(expected_02)

# %% 
print("1. Making the data structure")
class circular_array:
    """Circular array data structure."""

    def __init__(self, array: list):
        self.array_ = array


ca1 = circular_array([5, 3, 1, 1])



ca1.array_


# %% Circular distance
# Poderia se fazer um shift também.


# list -> int -> np.array
def circular_distance_array_from_idx(array: list,
                                     indx: int) -> np.array:
    """Calculate circular distance array from index."""

    n = len(array)

    array_indx = indx + 1
    index_array = np.arange(start=1, stop=n+1, step=1)

    forward_distance = np.abs(array_indx
                              - index_array)

    backwards_distance = n - forward_distance
    circular_distance = np.min(np.array([forward_distance,
                                         backwards_distance]),
                               axis=0)

    return circular_distance


test_circular_array = np.array([1, 2, 1,
                                0, 1, 2])
element_test_0 = 0
expected_distance_array_0 = [0, 1, 2,
                             3, 2, 1]

distance_0 = circular_distance_array_from_idx(array=test_circular_array,
                                              indx=element_test_0)
print(f'Distance from position 0: {distance_0}')
assert all(distance_0 == expected_distance_array_0)

element_test_1 = 1
expected_distance_array_1 = [1, 0, 1,
                             2, 3, 2]
distance_1 = circular_distance_array_from_idx(array=test_circular_array,
                                              indx=element_test_1)
print(f'Distance from position 1: {distance_1}')
assert all(distance_1 == expected_distance_array_1)

element_test_2 = 2
expected_distance_array_2 = [2, 1, 0,
                             1, 2, 3]

distance_2 = circular_distance_array_from_idx(array=test_circular_array,
                                              indx=element_test_2)
print(f'Distance from position 2: {distance_2}')
assert all(distance_2 == expected_distance_array_2)


# %% Get elements at circular distance of d from index i

d_test = 2

i_test_0 = 0
test_circular_array = np.array([1, 2, 1,
                                0, 1, 2])

expected_neighbours = [1, 2, 1, 1, 2]
distance_0 = circular_distance_array_from_idx(array=test_circular_array,
                                              indx=i_test_0)


print(distance_0)
distance_mask = distance_0 <= d
d_environment = test_circular_array[distance_mask]

print(distance_mask)
print(d_environment)


def get_d_environment_from_index(array: np.array,
                                 index: int,
                                 distance: int) -> np.array:
    """Get closest n elements from a circular array."""

    distance_array = circular_distance_array_from_idx(array=array,
                                                      indx=index)
    distance_mask = distance_array <= distance
    d_environment = test_circular_array[distance_mask]

    return d_environment


    
neighbours_from_0 = get_d_environment_from_index(array=test_circular_array,
                                                 index=i_test_0,
                                                 distance=d_test)

assert == d_enviroment


