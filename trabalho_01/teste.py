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


# %% 
print("1. Making the data structure")
class circular_array:
    """Circular array data structure."""

    def __init__(self, array: list):
        self.array_ = array


ca1 = circular_array([5, 3, 1, 1])



ca1.array_



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

# %% Read the input file

input = open('cell1.in', 'r')
input_data = input.readlines()

# %% Get params

parameters = input_data[0].replace('\n', '').split(' ')

modular = int(parameters[1])
d = int(parameters[2])
i = int(parameters[3].replace('\n', ''))

# %% Get the automaton

automaton = np.array([int(numeric_string) for numeric_string in input_data[1].split(' ')])

def get_d_environment_from_index(array: np.array,
                                 index: int,
                                 distance: int) -> np.array:
    """Get closest n elements from a circular array."""

    distance_array = circular_distance_array_from_idx(array=array,
                                                      indx=index)
    distance_mask = distance_array <= distance
    d_environment = array[distance_mask]

    return d_environment

result_array = automaton

for key in range(i):
    print('--------------------')
    # Set the aux as an empty array
    aux = np.array([])
    for index in range(len(automaton)):
        print('Current automaton ', result_array)
        neighbours = get_d_environment_from_index(array=result_array,
                                                    index=index,
                                                    distance=d)
        if(len(neighbours) > 0):
            aux = np.append(aux, int(np.sum(neighbours)%modular))
            print(f'Neighbours from position {index}: {neighbours}')

    result_array = aux[:]

result_string = ' '.join(np.array([str(int(numeric)) for numeric in result_array]))
print(result_string)


with open('cell.out', 'w+') as f:
    f.write(result_string)

print(f'Result array: {result_array}')
