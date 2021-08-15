from math import sqrt

def quad(a,b,c):
    ans1 =  (-b + sqrt(b**2 - 4*a*c))/(2*a)
    ans2 =  (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print('x1 = ', ans1, 'and x2 = ', ans2)
    return ans1, ans2

quad(2,7,-15)
