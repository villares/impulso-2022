
def setup():
    size(600, 600)
    background(255, 255, 200) # R, G, B

    cores = []  # lista vazia de cores
    for i in range(8):  # 0, 1, 2 ... 7
        cor = color(i * 32, 0, 255 - i * 32)
        cores.append(cor)
    print(len(cores))
    d = 70
    x = d
    for cor in cores:
        fill(cor)
        circle(x, 300, d)
        x = x + d
        