from math import sqrt

def cAdd(a,b):
    add = [a[0]+b[0],a[1]+b[1]]
    return add

def cMult(u,v):
    mult = [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
    return mult

def magnitud(z):
    mag = sqrt(z[0]**2+z[1]**2)
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


# range of x-values
xmin = -0.25
xmax = 0.25

# range fo y-values
ymin = -1
ymax = -0.5

# calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height

def draw():
    # origin in center
    translate(width/2,height/2)
    # go over all x's and y's on the grid
    for x in range(width):
        for y in range(height):
            z = [(xmin+x*xscl),(ymin+y*yscl)]
            # put it into the mandelbrot function
            col = mandelbrot(z,100)
            # if mandelbrot returns 0
            if col == 100:
                fill(0) # make the rectangle black
            else:
                fill(255-15*col,255,255) # make the rectangle white
            # draw a tiny rectangle 
            rect(x*xscl,y*yscl,1,1)
                    
                
