from scipy.optimize import minimize


print('minimize a function')


def func(vector):
    return vector[0]**2 + vector[1]**2

def func1(vector):
    return vector[0]**2 - vector[1]**2

def func2(x):
    return 2*x[0]**2 + 2*x[1]*x[0] + 2*x[1]**2 - 6*x[0]


def main():
    x0 = [2,3]
    res = minimize(func2, x0, method='nelder-mead')
    print(round(res.fun))
    print(res)


main()
