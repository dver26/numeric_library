def runge_kutta_2(a, b, n, y0, f):
    h = (b-a) / n
    y = [y0]

    for i in range(1, n+1):
        k1 = f(a + (i-1)*h, y[i-1])
        k2 = f(a + i*h, y[i-1] + h*k1)

        y.append(y[i-1] + (h/2)*(k1 + k2))

    return y

def runge_kutta_4(a, b, n, y0, f):
    h = (b-a) / n
    y = [y0]

    for i in range(1, n+1):
        k1 = f(a + (i-1)*h, y[i-1])
        k2 = f(a + (i-1)*h + h/2, y[i-1] + (h/2)*k1)
        k3 = f(a + (i-1)*h + h/2, y[i-1] + (h/2)*k2)
        k4 = f(a + (i-1)*h + h, y[i-1] + h*k3)

        y.append(y[i-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4))

    return y