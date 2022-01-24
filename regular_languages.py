

def afd(Q, Sigma, delta, q0, F, chain):
    """Simulates an finite deterministic automaton
        making it return False if a string is not part of its language.
    """

    qA = q0
    
    for s in chain:
        print(f'Reading {s}')
        qA = delta[(qA, s)]
        print(f'Next active state is {qA}')

    return qA in F


# Exercise 2

Q = ['q', 'q1', 'q0', 'q0.', 'q0..']

delta = {('q', '0'): 'q0',
         ('q', '1'): 'q1',

         ('q1', '0'): 'q1',
         ('q1', '1'): 'q1',

         ('q0', '0'): 'q0.',
         ('q0', '1'): 'q0.',

         ('q0.', '0'): 'q0..',
         ('q0.', '1'): 'q0..',

         ('q0..', '0'): 'q0..',
         ('q0..', '1'): 'q0..',
         }

F = ['q0..']
Sigma = ['0', '1']
q0 = 'q'
cadeia = '0001'
cadeia = '00'


afd(Q, Sigma, delta, q0, F, cadeia)
