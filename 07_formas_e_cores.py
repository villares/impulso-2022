from itertools import permutations
from itertools import product

w = 15
h = w * sqrt(3) / 2

def t(x, y):
    triangle(x - w / 2, y + h / 2,
             x + w / 2, y + h / 2,
             x, y - h / 2)

def q(x, y):
    square(x, y, w * 0.85)

def c(x, y):
    circle(x, y, w)

formas = [t, q, c]
cores = [color(0, 0, 200), color(0, 200, 0)]
cores_b = [color(0, 0, 200), color(200, 200, 0)]

def ordem(formas):
    (func_a, cor_a), (func_b, cor_b), (func_c, cor_c) = formas
    ordem_func = {t: 3, q: 2, c: 1}
    return (cor_a * ordem_func[func_a] * 100 +
            cor_b * ordem_func[func_b] * 10 +
            cor_c * ordem_func[func_c])
            
def setup():
    size(900, 660)
    background(0)
    no_stroke()
    rect_mode(CENTER)
    # permutacoes = permutations(formas, 3)
    formas_com_cores = list(product(formas, cores)) # (func, cor)
    produto_formas = list(product(formas_com_cores, repeat=3))
    formas_com_cores_b = list(product(formas, cores_b)) # (func, cor)
    produto_formas_b = list(product(formas_com_cores_b, repeat=3))
    print(len(produto_formas))
    x = y = w
    formas_combinadas = set(produto_formas + produto_formas_b)
    formas_ordenadas = sorted(formas_combinadas, key=ordem)
    for a in formas_ordenadas:
        arranjo(x, y, a)
        y = y + w * 1.5
        if y > height - w:
            y = w
            x = x + w * 4
    
def arranjo(x, y, formas):
    for func, cor in formas:
        fill(cor)
        func(x, y)
        x = x + w