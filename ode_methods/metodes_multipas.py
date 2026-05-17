import numpy as np

def runge_kutta_4(a, b, n, y0, f):
    h = (b - a) / n
    y = [y0]
    for i in range(1, n + 1):
        ti = a + (i - 1) * h
        k1 = f(ti,       y[i-1])
        k2 = f(ti + h/2, y[i-1] + (h/2)*k1)
        k3 = f(ti + h/2, y[i-1] + (h/2)*k2)
        k4 = f(ti + h,   y[i-1] + h*k3)
        y.append(y[i-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4))
    return y

def adams_bashforth_2(a, b, n, y0, f):
    h = (b - a) / n
    t = [a + i*h for i in range(n + 1)]
    y = runge_kutta_4(a, a + h, 1, y0, f)

    for i in range(1, n):
        f0 = f(t[i],   y[i])
        f1 = f(t[i-1], y[i-1])
        y.append(y[i] + (h/2) * (3*f0 - f1))

    return t, y

def adams_bashforth_4(a, b, n, y0, f):
    h = (b - a) / n
    t = [a + i*h for i in range(n + 1)]
    y = runge_kutta_4(a, a + 3*h, 3, y0, f)

    for i in range(3, n):
        f0 = f(t[i],   y[i])
        f1 = f(t[i-1], y[i-1])
        f2 = f(t[i-2], y[i-2])
        f3 = f(t[i-3], y[i-3])
        y.append(y[i] + (h/24) * (55*f0 - 59*f1 + 37*f2 - 9*f3))

    return t, y

def adams_moulton_4(a, b, n, y0, f, tol=1e-10, max_iter=50):
    h = (b - a) / n
    t = [a + i*h for i in range(n + 1)]

    y = runge_kutta_4(a, a + 3*h, 3, y0, f)

    for i in range(3, n):
        f0 = f(t[i],   y[i])
        f1 = f(t[i-1], y[i-1])
        f2 = f(t[i-2], y[i-2])
        f3 = f(t[i-3], y[i-3])
        y_pred = y[i] + (h/24) * (55*f0 - 59*f1 + 37*f2 - 9*f3)

        y_next = y_pred
        for _ in range(max_iter):
            y_new = y[i] + (h/24) * (9*f(t[i+1], y_next) + 19*f0 - 5*f1 + f2)
            if abs(y_new - y_next) < tol:
                y_next = y_new
                break
            y_next = y_new

        y.append(y_next)

    return t, y

def predictor_corrector(a, b, n, y0, f):
    h = (b - a) / n
    t = [a + i*h for i in range(n + 1)]

    # Arrencada: primers 4 punts
    y = runge_kutta_4(a, a + 3*h, 3, y0, f)

    for i in range(3, n):
        f0 = f(t[i],   y[i])
        f1 = f(t[i-1], y[i-1])
        f2 = f(t[i-2], y[i-2])
        f3 = f(t[i-3], y[i-3])

        y_pred = y[i] + (h/24) * (55*f0 - 59*f1 + 37*f2 - 9*f3)

        y_corr = y[i] + (h/24) * (9*f(t[i+1], y_pred) + 19*f0 - 5*f1 + f2)

        y.append(y_corr)

    return t, y

if __name__ == "__main__":
    f = lambda t, y: -y
    exacta = lambda t: np.exp(-t)

    a, b, n, y0 = 0, 2, 20, 1

    t_ab2, y_ab2 = adams_bashforth_2(a, b, n, y0, f)
    t_ab4, y_ab4 = adams_bashforth_4(a, b, n, y0, f)
    t_am4, y_am4 = adams_moulton_4(a, b, n, y0, f)
    t_pc,  y_pc  = predictor_corrector(a, b, n, y0, f)

    print(f"{'t':>6}  {'Exacta':>12}  {'AB2':>12}  {'AB4':>12}  {'AM4':>12}  {'PC':>12}")
    print("-" * 70)
    for i in range(n + 1):
        t_i = a + i*(b-a)/n
        ye  = exacta(t_i)
        print(f"{t_i:6.3f}  {ye:12.8f}  {y_ab2[i]:12.8f}  {y_ab4[i]:12.8f}  {y_am4[i]:12.8f}  {y_pc[i]:12.8f}")
