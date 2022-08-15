#!/usr/bin/env python
# coding: utf-8

# In[1]:


## a program to calculate the fractal dimension of an image
## using the differential box-counting method 
## described in Y. Liu et al (2014)


# In[2]:


import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy import optimize as opt


# In[3]:


# load image and convert into array

#img_data = fits.getdata('test_grayscale.fits') # grayscale testing image
#img_data = fits.getdata('test_image.fits') # anticross-stitch fractal
#img_data = fits.getdata('test_3.fits')
img_data = fits.getdata('D112.fits')


# In[4]:


#img_data = np.random.randint(0, high=255, size=(12,12))
img_data


# In[5]:


print(type(img_data))
[m,n]=img_data.shape
print([m,n])


# In[6]:


print(img_data)


# In[7]:


#plt.imshow(img_data, cmap='gray')
#plt.colorbar()


# In[8]:


from sympy import divisors
s = divisors(m)
s.pop(0) # 1 is a trivial divisor
s.pop() # so is the number itself
 # this is the pixel width of each grid box
s


# In[9]:


# define number of gray levels
GMax = np.max(img_data)
GMin = np.min(img_data)
G = GMax - GMin + 1 # Total number of gray levels in entire image


# In[10]:


## a function for counting the number of boxes of size x by y by h
# needed to cover the image at that grid box
def countSingle(img_data,x,y,h,s,k):
    box_count = 0
    loc_grid=[]
    for j in range(s[k]):
        for i in range(s[k]):
            loc_grid.append(img_data[x+j,y+i])
        #print(loc_grid)
    loc_max = np.max(loc_grid)
    loc_min = np.min(loc_grid)
    g_range = loc_max - loc_min + 1 # local gray level range
    #print("The local gray level range is:", g_range)
    if g_range == 1:
        box_count += 1
    else:
        box_count += (np.ceil(g_range/h))
    # print("The total box count is:", box_count)
    return box_count
    


# In[13]:


def countAll(img_data,s):
    k = 0 # index for grid box width s
    n_r = [] # list of box counts for a given k
    N_r = [] # list of total least number of boxes to cover image 
    r = [] # list of ratios
    while k < len(s) and s[k] < m/2:
        h = (s[k] * G) / m # height of box in z-direction
        r.append(s[k] / m) # ratio, scale
        scales = np.reciprocal(r)
        print('grid box width is:', s[k])
        print('image grid size is:', m/s[k], 'by', n/s[k])
        for j in range(int(scales[k])):
             for i in range(int(scales[k])):
                x_mult = j * s[k]
                y_mult = i * s[k]
                box_count = countSingle(img_data,x_mult,y_mult,h,s,k);
                n_r.append(box_count)
        #print(n_r)
        N_r.append(sum(n_r))
        n_r = []
        #print(N_r)
        k = k+1
        #print(r)
        #print(scales)
    return N_r, scales, r
    


# In[15]:


(N_total, scales, r) = countAll(img_data,s)
print('The number of boxes needed to cover the surface is: \n',N_total)


# In[19]:


#def linear_fit(x,a,b):
#    y = a*x +b
#    return y
#alpha = opt.curve_fit(linear_fit, xdata= np.log(scales), ydata=np.log(N_total))[0]
#print(alpha)
#print(np.log(-1* alpha[0]))


# In[23]:


fit = np.polyfit(np.log(scales),np.log(N_total),1)
plt.plot(np.log(scales),np.log(N_total), 'o', mfc='none')
plt.plot(np.log(scales), np.polyval(fit, np.log(scales)))
plt.xlabel('$\log 1/r$')
plt.ylabel('$\log N_r$')
plt.show()
print(fit) # the fractal dimension is the negative of the fitting coefficient
print('The fractal dimension is', fit[0])


# In[22]:


fit = np.polyfit(np.log(r),np.log(N_total),1)
plt.plot(np.log(r),np.log(N_total), 'o', mfc='none')
plt.plot(np.log(r), np.polyval(fit, np.log(r)))
plt.xlabel('$\log r$')
plt.ylabel('$\log N_r$')
plt.show
print(fit) # the fractal dimension is the negative of the fitting coefficient
print('The fractal dimension is', -1 * fit[0])


# In[21]:


fit = np.polyfit(np.log(r),np.log(N_total),1)
plt.plot(scales,np.log(N_total), 'o', mfc='none')
plt.plot(scales, np.polyval(fit, np.log(r)))
plt.xlabel('$1/r$')
plt.ylabel('$\log N_r$')
plt.show
print(fit) # the fractal dimension is the negative of the fitting coefficient
print('The fractal dimension is', -1 * fit[0])


# In[ ]:




