

# list -> int -> np.array
def circular_distance_py(array: list,
                         indx: int) -> list:
    """Calculate circular distance array from index
       in pure python."""

    n = len(array)

    array_indx = indx + 1
    index_array = list(range(1, n+1, 1))

    forward_distance = [abs(array_indx - i) for i in index_array]
    backwards_distance = [n - i for i in forward_distance]

    circular_distance = ([min([i, j]) for i, j
                        in zip(forward_distance, backwards_distance)])

    return circular_distance

# %% Read the input file
input = open('cell.in', 'r')
input_data = input.readlines()

# %% Get params
parameters = input_data[0].replace('\n', '').split(' ')

modular = int(parameters[1])
d = int(parameters[2])
i = int(parameters[3].replace('\n', ''))

# %% Get the automaton
automaton =[int(numeric_string) for numeric_string in input_data[1].split(' ')]

def get_d_environment_py(array: list,
                         index: int,
                         d: int) -> list:
    """Get closest n elements from a circular array."""

    distances = circular_distance_py(array, index)

    d_environment = ([element for element, distance in zip(array, distances)
                              if distance <= d])

    return d_environment

#initial automaton
result_array = automaton

#For each step, set the current state
for key in range(i):
    # Set the aux as an empty array
    aux = []
    # For each position in the automaton, get the new value
    for index in range(len(automaton)):
        print('Current automaton ', result_array)
        # Gete the d closest neighbors
        neighbours = get_d_environment_py(array=result_array,
                                          index=index,
                                          d=d)
        # If exists at least one neighbor, set the value for the current position
        if(len(neighbours) > 0):
            aux.append(sum(neighbours) % modular)
            print(f'Neighbours from position {index}: {neighbours}')

    result_array = aux[:]

result_string = ' '.join([str(int(numeric)) for numeric in result_array])
print(result_string)

with open('cell.out', 'w+') as f:
    f.write(result_string)

print(f'Result array: {result_array}')
print(f'Steps: {i}')
