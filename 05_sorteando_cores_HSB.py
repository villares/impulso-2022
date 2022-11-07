from random import choice, shuffle, sample

def setup():
    size(600, 600)
    color_mode(HSB) # Hue (Matiz), Saturation, Brightness (Brilho)
    for i in range(8):
        cor = color(i * 32, 200, 200) # monta uma cor H, S, B
        cores.append(cor)

#     shuffle(cores)  # "embaralha" as cores
#     w = 75
#     for i, cor in enumerate(cores):  # indice, item
#        fill(cor)
#        rect(i * w, 0, w, height)

    w = 75
    for i in range(8):
        # cor_a = choice(cores)  # escolhe, "sorteia", uma cor
        # cor_b = choice(cores)  # outra cor
        cor_a, cor_b = sample(cores, 2)  # amostra, "sorteia" cores distintas
        fill(cor_a)
        rect(i * w, 0, w, height / 2)
        fill(cor_b)
        rect(i * w, height / 2, w, height / 2)

