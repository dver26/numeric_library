import numpy as np

def simpson_simple(a, b, f):
    return ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))

def simpson_compost(a, b, f, I):
    h = ((b-a)/I)
    nodes = [a+i*h for i in range(0, I+1)]
    sumatori_nodes = sum([f(x) for x in nodes[1:-1]])
    nodes_intermitjos = []
    for i in range(I):
        nodes_intermitjos.append(f((nodes[i] + nodes[i+1])/2))
    sumatori_intermitjos = sum(nodes_intermitjos)
    
    # Diferent a la fórmula del formulari
    return (h/6)*(f(a) + 4*sumatori_intermitjos + 2*sumatori_nodes + f(b))