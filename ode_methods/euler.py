def euler_method(a, b, n, y0, f):
    h = (b-a)/n
    y = [y0]

    for i in range(1, n+1):
        y.append(y[i-1] + h*f(a+(i-1)*h, y[i-1]))

    return y

def modified_euler_method(a, b, n, y0, f):
    h = (b-a)/n
    y = [y0]

    for i in range(1, n+1):
        y.append(y[i-1] + (h/2)*(f(a + (i-1)*h, y[i-1]) + f(a+i*h, y[i-1]+h*f(a+(i-1)*h, y[i-1]))))

    return y