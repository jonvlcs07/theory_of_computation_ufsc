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
                          distances: list) -> list:
        """Get closest n elements from a circular array."""

        #distances = self._circular_distance(array, index)

        d_environment = ([element for element, distance in zip(array, distances)
                                  if distance <= self.d])

        return d_environment

    def _findSum(self, arr, N):
         if len(arr)== 1:
            return arr[0]
         else:
            return arr[0]+self._findSum(arr[1:], N)

    def _environment_sum(self,
                        array: list,
                        distances: list) -> int:
        """Module sum elements from environment"""

        d_environment = self._get_d_environment(array, distances)
        N = len(d_environment)
        enviroment_module_sum = (self._findSum(d_environment, N)
                                 % self.modulo)

        return enviroment_module_sum


    def _dynamic_environment_sum(self,
                                 array: list,
                                 index: int,
                                 distances: list) -> int:
        """Module sum elements from environment"""

        if (tuple(array), index) in self.cache.keys():
            next_cell = self.cache[(tuple(array), index)]

        else:
            next_cell = self._environment_sum(array, distances)
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

 # Return sum of elements in A[0..N-1]
 # using recursion.
current_automaton = automaton

automatonCache = {}
distances = {}

for key in range(i):
    # print('--------------------')
    # Set the aux as an empty array
    aux = []
    for index in range(len(automaton)):
        if (index not in distances.keys()):
            distances[index] = ds._circular_distance(current_automaton, index)
        sum_ = ds._dynamic_environment_sum(current_automaton, index, distances[index])
        aux.append(sum_)
        print(f'Neighbours from position {index}: {sum_}')

    automatonCache[(tuple(current_automaton))] = aux
    current_automaton = aux

result_string = ' '.join([str(int(numeric)) for numeric in current_automaton])
print(result_string)

with open('cell.out', 'w+') as f:
    f.write(result_string)
