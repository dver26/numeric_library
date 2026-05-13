def trapezis_simple(a, b, f):
    return ((b-a) / 2)*(f(a) + f(b))

def trapezis_compost(a, b, f, n):
    h = (b-a) / n
    nodes = [a + (k)*((b-a)/n) for k in range(1, n)]
    return (h / 2)*(f(a) + 2*sum([f(x) for x in nodes]) + f(b))