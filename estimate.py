import numpy as np
from math import log2, comb
import matplotlib.pyplot as plt
n = 100000 #Global
def cheon_exponent(x):
    return 0.21
def cheon_data(x):
    return 0.21
def h(p):
    if p == 0 or p ==1:
        return 0
    else:
        return -p*log2(p) - (1-p)*log2(1-p)
def memory(alpha):
    return (1.41*alpha*n + n +2.34 - log2(comb(n, int(alpha*n))) - log2(comb(int(alpha*n), int(alpha*n/2))))/(2*n)
def exponent(alpha):
    Mem = (1.41*alpha*n + n +2.34 - log2(comb(n, int(alpha*n))) - log2(comb(int(alpha*n), int(alpha*n/2))))/2 
    Lambda = Mem/n
    if(1 - h(alpha/2) < Lambda):
        return 1
    else:
        approx = 1/2 * (1-np.sqrt(1- (1-Lambda)**(4/3))) #Approximation of the inverse entropy function, reduce the error to less than 10^-3
        while(abs(h(approx) - (1-Lambda)) > 0.001):
            approx = approx - 0.001
        
    return (1-alpha)*(1- h((approx-alpha/2)/(1-alpha)))
def complexity(alpha):
    y = exponent(alpha)
    return y*n

#https://math.stackexchange.com/questions/188195/inverse-of-binary-entropy-function-for-0-le-x-le-frac12
if __name__=='__main__':
    x = np.arange(0.1, 0.5, 0.001)
    y1 = np.vectorize(memory)
    y2 = np.vectorize(cheon_data)
    plt.plot(x, y1(x), label ='Our attack')
    plt.plot(x, y2(x), label = "Cheon et al.", linestyle ='--')
    plt.legend(loc="upper right")
# naming the x axis
    plt.xlabel(r'$\alpha$')
# naming the y axis
    plt.ylabel(r'$Data complexity \lambda /n$')
  
# giving a title to my graph
    plt.title(r'$n = 100000$')
    
# function to show the plot
    plt.savefig("100000data.png")
    
    """alpha = 0.22
    mem = (1.41*alpha*n + n +2.34 - log2(comb(n, int(alpha*n))) - log2(comb(int(alpha*n), int(alpha*n/2))))/2 
 
    print("List size need:", mem)
    lam = mem/n

    print("Check:" )
    print("1 - H(alpha/2):", 1- h(alpha/2))
    print("lambda:", lam)
    if(1-h(alpha/2) > lam):
        print("Condition OK ")
    else:
        print("CONDITION WRONG")
    print("1- lambda:", 1-lam)
    approx = 0.3033
    approx = 1/2 * (1-np.sqrt(1- (1-lam)**(4/3)))
    while(abs(h(approx) - (1-lam)) > 0.001):
        approx = approx - 0.001
    print(h(approx))
    print(approx)
    y = (1-alpha)*(1- h((approx-alpha/2)/(1-alpha)))
    print("y: ", y)
    #c = y*n 
    #print("cost: ", c)"""
    
    
    
    
    ##min alpha = 0.18, max = 0.68
    #alpha = 0.43, c = 42.13 approx 1-lambda = 0.890266, h-1(1-lambda) approx 0.3075, cost = 78.85
    #alpha = 0.35, c = 45.96, approx 1-lambda = 0.88029, h-1(1-lambda) approx 0.29919, cost = 73.95
    #alpha = 0.3, c = 52, 1-lambda =   0.86477, h-1 approx 0.28697, cost = 77.1
    #alpha = 0.25, c = 61.1, 1-lambda = 0.8408, h-1 approx 0.2696, cost = 84.3
    #best_alpha = 0.37, c = 44.07, 1- lambda = 0.8852240, h-1(1-lambda) approx = 0.3033. cost = 73.35
    #asymptotic y:
    # n = 30000, alpha in (0.23,)
    #n = 20000, alpha in (0.23, 0.49)
    # n = 15000, alpha in (0.23, 0.49)
    # n= 10000, alpha in (0.23,0.49)
    # n = 1000, alpha in (0.24, 0.47
    # n = 500, alpha in (0.25, 0.46)
    # n = 10000
    
    
    """y= 1.0
    c = 80
    params =[0.0,0.0,0.0,0.0,0.0]
    for alpha in np.linspace(0.20,0.5,31):
    	mem = (1.41*alpha*n + n +2.34 - log2(comb(n, int(alpha*n))) - log2(comb(int(alpha*n), int(alpha*n/2))))/2
    	lam = mem/n
    	if 1-h(alpha/2)> lam:
    		approx = 1/2 * (1-np.sqrt(1- (1-lam)**(4/3)))
    		y_temp = (1-alpha)*(1- h((approx-alpha/2)/(1-alpha)))
    		c_temp = y_temp*n
    		if c_temp < c:
    			c = c_temp
    			params[0] = mem
    			params[1] = alpha
    			params[2] = 1-lam
    			params[3] = approx
    			params[4] = c_temp
    
    print("mem: ", params[0], "alpha: ", params[1], " 1-lam: ", params[2], "approx: ", params[3], "compl: ", params[4])"""		
    	   	   	 

    """ def binary_entropy_nats(prob): 
    return -prob*np.log(prob) - (1-prob)*np.log(1-prob) 
 
def binary_entropy_nats_prime(prob): 
    return np.log((1-prob)/prob) 
 
def inverse_binary_entropy_nats(entropy_val, num_iter=3): 
    guess = (np.arcsin((entropy_val/np.log(2))**(1/.645)))/np.pi 
    for i in range(num_iter): 
        guess = guess + np.nan_to_num((entropy_val-binary_entropy_nats(guess))/binary_entropy_nats_prime(guess)) 
    return guess  """
