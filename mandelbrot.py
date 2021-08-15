from math import sqrt

def cAdd(a,b):
    add = [a[0]+b[0],a[1]+b[1]]
    print(str(add))
    return add

def cMult(u,v):
    mult = [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
    print(str(mult))
    return mult

def magnitud(z):
    mag = sqrt(z[0]**2+z[1]**2)
    print(str(mag))
    return mag

def mandelbrot(z,num):
    """runs the process num times
    and returns the diverge count"""
    count = 0
    # define z1 as z
    z1 = z
    # iterate num times
    while count <= num:
        # check for divergence
        if magnitud(z1) > 2.0:
            # return the step it deverged on
            return count
        # iterate z
        z1 = cAdd(cMult(z1,z1),z)
        count += 1
        # if z hasn't diverged by the end
        return num

mandelbrot([0.25,0.75],5)