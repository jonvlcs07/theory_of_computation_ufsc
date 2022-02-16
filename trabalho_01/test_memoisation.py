"""
Testando algumas técnicas de memoização para o trabalho 1
de teoria da computação.


"""

# %% Armazenando o problema na tabela
# Cache -> tabela que mostra quais os problemas que foram resolvidos
# e o resultado deles


p2 = (1, (1,  2, 3, 4, 5))
r1 = sum(p1)

cache = {}

# Armazenando um problema no cache
cache[p1] = r1
p2 = (1, (1,  2, 3, 4, 6))

_ = p2 in cache.keys()
print(f"Problema p2 está no cache? {_}")

_ = p1 in cache.keys()
print(f"Problema p1 está no cache? {_}")

# É possível armazenar o problema em uma tabela desde que ele fique como
# uma tupla.


# %% Definitions

def circular_distance(array: list,
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


def get_d_environment(array: list,
                      index: int,
                      d: int) -> list:
    """Get closest n elements from a circular array."""

    distances = circular_distance(array, index)

    d_environment = ([element for element, distance in zip(array, distances)
                              if distance <= d])

    return d_environment


def environment_sum(array: list,
                    index: int,
                    d: int,
                    module: int) -> int:
    """Module sum elements from environment"""

    d_environment = get_d_environment(array, index, d)
    enviroment_module_sum = sum(d_environment) % module

    return enviroment_module_sum


def dynamic_environment_sum(array: list,
                            index: int,
                            d: int,
                            module: int) -> int:
    """Module sum elements from environment"""

    cache = {}

    if 
    d_environment = get_d_environment(array, index, d)
    enviroment_module_sum = sum(d_environment) % module

    return enviroment_module_sum
    
