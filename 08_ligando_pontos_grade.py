from itertools import product, combinations


grade = list(product((-1, 0, 1, 2), (-1, 0, 1, 2)))

def sq_dist_linha(linha):
    (ia, ja), (ib, jb) = linha
    return (ia - ib) ** 2 + (ja - jb) ** 2

def setup():
    size(560, 700)
    
    xc = yc = 50
    w = 10
            
    linhas = list(combinations(grade, 2))
    linhas.sort(key=sq_dist_linha)
    print(len(linhas))
    
    for linha in linhas:
        stroke(0)
        stroke_weight(5)
        for i, j in grade:
            x = xc + i * w
            y = yc + j * w
            point(x, y)
        (ia, ja), (ib, jb) = linha
        stroke(255)
        stroke_weight(5)
        xa, ya = xc + ia * w, yc + ja * w
        xb, yb = xc + ib * w, yc + jb * w
        line(xa, ya, xb, yb)
        no_stroke()
        fill(255)
        circle(xa, ya, 8)
        circle(xb, yb, 8)
        
        xc = xc + w * 5
        if xc > width - w * 2:
            xc = 50
            yc = yc + w * 5







    