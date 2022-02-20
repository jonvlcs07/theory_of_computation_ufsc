class DynamicEnvironmentSum:

    def __init__(self,
                 modulo: int,
                 d: int):

        self.modulo = modulo
        self.d = d
        self.cache = {}


    def _circular_distance(self,
                          array: list,
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


    def _get_d_environment(self,
                          array: list,
                          index: int) -> list:
        """Get closest n elements from a circular array."""

        distances = self._circular_distance(array, index)

        d_environment = ([element for element, distance in zip(array, distances)
                                  if distance <= self.d])

        return d_environment


    def _environment_sum(self,
                        array: list,
                        index: int) -> int:
        """Module sum elements from environment"""

        d_environment = self._get_d_environment(array, index)
        enviroment_module_sum = sum(d_environment) % self.modulo

        return enviroment_module_sum


    def _dynamic_environment_sum(self,
                                 array: list,
                                 index: int) -> int:
        """Module sum elements from environment"""


        if (tuple(array), index) in self.cache.keys():
            next_cell = self.cache[(tuple(array), index)]

        else:
            next_cell = self._environment_sum(array, index)
            self.cache[(tuple(array), index)] = next_cell

        return next_cell


input = open('cell.in', 'r')
input_data = input.readlines()

parameters = input_data[0].replace('\n', '').split(' ')

modular = int(parameters[1])
d = int(parameters[2])
i = int(parameters[3].replace('\n', ''))

automaton =[int(numeric_string) for numeric_string in input_data[1].split(' ')]
result_array = automaton

ds = DynamicEnvironmentSum(modulo=modular,
                           d=d)

current_automaton = automaton

for key in range(i):
    # print('--------------------')
    # Set the aux as an empty array
    aux = []
    for index in range(len(automaton)):
        sum_ = ds._dynamic_environment_sum(current_automaton, index)
        aux.append(sum_)
        # print(f'Neighbours from position {index}: {sum_}')

    current_automaton = aux

result_string = ' '.join([str(int(numeric)) for numeric in current_automaton])
# print(result_string)

with open('cell.out', 'w+') as f:
    f.write(result_string)


