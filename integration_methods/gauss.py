import numpy as np

def pol_legendre(n, x):
    if n == 0: return 1
    elif n == 1: return x

    pn_2 = 1
    pn_1 = x

    for i in range(2, n+1):
        p_n = (1/i) * ((2*i-1) * x * pn_1 - (i-1)*pn_2)
        pn_1, pn_2 = p_n, pn_1

    return pn_1

def derivada_pol_legendre(n, x):
    if n == 0: return 0
    elif n == 1: return 1

    pn_2 = 1
    pn_1 = x

    dpn_2 = 0
    dpn_1 = 1

    for i in range(2, n+1):
        p_n = (1/i) * ((2*i-1) * x * pn_1 - (i-1)*pn_2)
        dp_n = ((2*i-1) * (pn_1 + x * dpn_1) - (i-1) * dpn_2) / i
        pn_1, pn_2 = p_n, pn_1
        dpn_1, dpn_2 = dp_n, dpn_1

    return dpn_1

def pesos_legendre(m: int, x: list[float]):
    pesos  = []
    for i in range(0, m+1):
        der = derivada_pol_legendre(m+1, x[i])
        pesos.append(2 / ((1 - x[i]*x[i]) * der * der))

    return pesos

def zeros_legendre(n):
    raices = []
    for k in range(1, n//2 + 1):
        # Estimación inicial
        x = np.cos(np.pi * (k - 0.25) / (n + 0.5))
        # Newton-Raphson
        for _ in range(100):
            dx = -pol_legendre(n, x) / derivada_pol_legendre(n, x)
            x += dx
            if abs(dx) < 1e-15: break
        raices.append(x)
    
    # Simetría
    raices = np.array(raices)
    if n % 2 == 0:
        raices = np.concatenate([-raices, raices[::-1]])
    else:
        raices = np.concatenate([-raices, [0], raices[::-1]])
    
    return np.sort(raices)