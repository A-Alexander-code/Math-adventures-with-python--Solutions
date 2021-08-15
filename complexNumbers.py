from math import sqrt

def cAdd(a,b):
    add = [a[0]+b[0],a[1]+b[1]]
    print(str(add))
    return add

u = [1,2]
v = [3,4]

cAdd(u,v)

def cMult(u,v):
    mult = [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
    print(str(mult))
    return mult

i = [1,2]
j = [3,4]

cMult(i,j)

def magnitud(z):
    mag = sqrt(z[0]**2+z[1]**2)
    print(str(mag))
    return mag

magnitud([2,1])

z = [0.25,1.5]
z2 = cMult(z,z)
z2

ans1 = cAdd(z2,z)

magnitud(ans1)

print('------')

m = [0.25,0.75]
m2 = cMult(m,m)
m3 = cAdd(m2,m)
magnitud(m3)