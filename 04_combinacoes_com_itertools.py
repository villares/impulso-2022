from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product

frutas = ['uva', 'banana', 'maçã', 'kiwi']  # uma lista de strings

combos = list(combinations(frutas, 2))
permutacoes = list(permutations(frutas, 2))
cwr = list(combinations_with_replacement(frutas, 2))
produto = list(product(frutas, repeat=2)) # equivale product(frutas, frutas)

# Exemplo de product() provendo coordenadas de uma grade
def setup():
    size(400, 400)
    for x, y in product((100, 200, 300), (50, 150, 250, 350)):
        circle(x, y, 100)
    
print(f'{len(combos)} combinações de frutas, duas a duas')
print(combos)
print(f'{len(permutacoes)} permutações de frutas, duas a duas')
print(permutacoes)
print(f'{len(cwr)} combinações, com substituição, de frutas, duas a duas')
print(cwr)
print(f'{len(produto)} produto frutas x frutas')
print(produto)
