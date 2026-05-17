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

def taylor_order_2(a, b, n, y0, f, df):
    h = (b-a) / n
    y = [y0]

    for i in range(1, n+1):
        T = f(a + (i-1)*h, y[i-1]) + (h/2) * df(a + (i-1)*h, y[i-1])
        y.append(y[i-1] + h*T)

    return y

def taylor_order_4(a, b, n, y0, f, df, d2f, d3f):
    h = (b-a) / n
    y = [y0]

    for i in range(1, n+1):
        T = f(a + (i-1)*h, y[i-1]) + (h/2) * df(a + (i-1)*h, y[i-1]) + ((h*h)/6) * d2f(a + (i-1)*h, y[i-1]) + ((h*h*h)/24)*d3f(a + (i-1)*h, y[i-1])
        y.append(y[i-1] + h*T)