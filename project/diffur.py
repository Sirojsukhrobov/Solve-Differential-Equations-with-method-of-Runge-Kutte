def f(x,y):
    return 2*(x**2)+0.1*x*y


def rk4(x0,y0,xn,n):
    h = (xn-x0)/n

    print('\n--------РЕШЕНИЕ--------')
    print('-------------------------')
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        print('-------------------------')

        y0 = yn
        x0 = x0+h
    print('\nx=%.4f, y=%.4f' %(xn,yn))


print('ВВЕДИТЕ НАЧАЛЬНЫЕ ЗНАЧЕНИЯ:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
print('ВВЕДИТЕ ТОЧКУ РАСЧЁТА: ')
xn = float(input('xn = '))
print('ВВЕДИТЕ ТОЧНОСТЬ ВЫЧИСЛЕНИЯ: ')
epsi = float(input('eps = '))
step = round(((xn-x0)/epsi)**(1/5))
print('\nКОЛИЧЕСВТО ШАГОВ РАВЕН:', step)
rk4(x0,y0,xn,step)