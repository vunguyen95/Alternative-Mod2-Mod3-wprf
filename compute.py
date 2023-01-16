import numpy as np
import cmath
import math
if __name__ == '__main__':
    l = 6 #6,12,18 OK
    real = math.cos((cmath.pi)/3) 
    img= math.sin((cmath.pi)/3)
    w = complex(real,img)
    temp = complex(0,math.sqrt(3))
    e0 = (w**(1*l)) * (1+w**1)**l + (w**(2*l)) * (1+w**2)**l + (w**(3*l)) * (1+w**3)**l + (w**(4*l)) * (1+w**4)**l + (w**(5*l)) * (1+w**5)**l
    #print(e0) OK
    #print(2+ 2*(math.sqrt(3))**l) #even
    e1 = (w**(1*(l-1))) * (1+w**1)**l + (w**(2*(l-1))) * (1+w**2)**l + (w**(3*(l-1))) * (1+w**3)**l + (w**(4*(l-1))) * (1+w**4)**l + (w**(5*(l-1))) * (1+w**5)**l
    #print(e1) OK
    #print((math.sqrt(3)**l - 1))
    e2 = (w**(1*(l-2))) * (1+w**1)**l + (w**(2*(l-2))) * (1+w**2)**l + (w**(3*(l-2))) * (1+w**3)**l + (w**(4*(l-2))) * (1+w**4)**l + (w**(5*(l-2))) * (1+w**5)**l
    #print(e2) #OK
    #print((-math.sqrt(3)**l - 1))# even
    e3 = (w**(1*(l-3))) * (1+w**1)**l + (w**(2*(l-3))) * (1+w**2)**l + (w**(3*(l-3))) * (1+w**3)**l + (w**(4*(l-3))) * (1+w**4)**l + (w**(5*(l-3))) * (1+w**5)**l
    #print(e3) #OK
    #print(-2*(math.sqrt(3)**l) + 2)
    e4 = (w**(1*(l-4))) * (1+w**1)**l + (w**(2*(l-4))) * (1+w**2)**l + (w**(3*(l-4))) * (1+w**3)**l + (w**(4*(l-4))) * (1+w**4)**l + (w**(5*(l-4))) * (1+w**5)**l
    #print(e4) #OK
    #print((-math.sqrt(3)**l - 1))# even
    e5 = (w**(1*(l-5))) * (1+w**1)**l + (w**(2*(l-5))) * (1+w**2)**l + (w**(3*(l-5))) * (1+w**3)**l + (w**(4*(l-5))) * (1+w**4)**l + (w**(5*(l-5))) * (1+w**5)**l
    #print(e5) #OK
    #print((math.sqrt(3)**l - 1))# even
    p0 = (e0**2 + e1**2 + e2**2 + e3**2 + e4**2 + e5**2) / (36*(4**l))
    #print(p0) # OK
    p1 = (e0*e1 + e1*e2 + e2*e3 + e3*e4 + e4*e5 + e5*e0) / (36*(4**l))
    #print (p1) #OK
    p2 = (e0*e2 + e1*e3 + e2*e4 + e3*e5 + e4*e0 + e5*e1) / (36*(4**l))
    #print(p2) #OK
    p3 = (e0*e3 + e1*e4 + e2*e5 + e3*e0 + e4*e1 + e5*e2) / (36*(4**l))
    #print(p3) #OK
    p4 = (e0*e4 + e1*e5 + e2*e0 + e3*e1 + e4*e2 + e5*e3) / (36*(4**l))
    #print(p4) #OK
    p5 = (e0*e5 + e1*e0 + e2*e1 + e3*e2 + e4*e3 + e5*e4) / (36*(4**l))
    #print(p5)
    prob = ((p0 + p1 + p2) + (p5 + p0 + p1) + (p4 + p5 + p0) + 3/2) 
    check = 3/2 + (3/4)**(l-1)
    print("Check:" )
    print((prob - check).real)
    print((1/3*prob - 1/2).real)
    #print((1 - 3**l) / (3 * 4**l))
    
    