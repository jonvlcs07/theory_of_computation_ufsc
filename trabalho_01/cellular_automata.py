'''
Trabalho 01 Teoria da Computação


Wish_list:
    - Cellular automata (Class):
        - Init
        - Sum n closest elements
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


# %% 
print("1.1 Circular distance")

# list -> int -> list
test_circular_array = [1, 2, 1,
                       0, 1, 2]
element_test = 1

expected_distance_array_1 = [0, 1, 2,
                             3, 2, 1]

n = len(expected_distance_array_1)

index_array = np.arange(start=1, stop=n, step=1)

forward_distance = np.abs(element_test
                          - index_array)
backwards_distance = n - forward_distance
print(f'Forward distance {forward_distance}')
print(f'Backwards distance {backwards_distance}')

concat = np.min(np.ndarray([forward_distance, backwards_distance]))
print(concat)

np.array([forward_distance, backwards_distance])


def circular_distance_array_from_idx(array: list,
                                     indx: int) -> list:
    """Calculate circular distance array from index."""


    n = len(array)
    index_array = np.arange(start=1, stop=n, step=1)

    return None

    
    









