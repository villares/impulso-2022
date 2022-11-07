
def setup():
    size(600, 600)            # Define o tamanho da área de desenho
    background(255, 255, 200) # R, G, B

    cores = []          # lista vazia para por as cores
    for i in range(8):  # repete fazendo i valer: 0, 1, 2 ... 7
        cor = color(i * 32, 0, 255 - i * 32)  # monta uma cor R, G, B
        cores.append(cor)  # acrescente `cor` ao final da lista cores
    print(len(cores))   # exibe no console o número de itens na lista
    d = 70
    x = d 
    for cor in cores:
        fill(cor)
        circle(x, 300, d)   # desenha círculo y:300 diâmetro:d (70)
        x = x + d  # pode ser escrito `x += d` também
        