#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#David Lipkin
#11/20/2019
#Homework 6 for PIC 16
#Professor Ji


# In[ ]:


def detect_edge(im, method):
    """
    detect_edge(im, method) takes a gray-scale image and detects edges,
    with the option of horizontal, vertical or both.
    """

    get_ipython().magic(u'matplotlib inline')
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
    
    n,m = im.shape
    output = np.empty([n,m], dtype = 'float64')
    
    if method == 'vertical':
        filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]]) #Sets standard vertical edge filter
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                output[i,j] = np.sum(filter * (im[i-1: i+2, j-1: j+2]))
                if output[i,j] > 0:
                    output[i,j] = 1 #Sets positive edges to white
                if output[i,j] == 0:
                    output[i,j] = 0.5 #Sets neutral pixels to grey
                if output[i,j] < 0:
                    output[i,j] = 0 #Sets negative edges to black
                
    if method == 'horizontal':
        filter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) #Sets standard horizontal edge filter
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                output[i,j] = np.sum(filter * (im[i-1: i+2, j-1: j+2]))
                if output[i,j] > 0:
                    output[i,j] = 1 #Sets positive edges to white
                if output[i,j] == 0:
                    output[i,j] = 0.5 #Sets neutral pixels to grey
                if output[i,j] < 0:
                    output[i,j] = 0 #Sets negative edges to black

    if method == 'both':
        filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]]) + np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) #Combines vertical and horizontal edge filters
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                output[i,j] = np.sum(filter * (im[i-1: i+2, j-1: j+2]))
                if output[i,j] < 0:
                    output[i,j] *= -1 #Removes distinction between positive and negative edges
                
    grey_output = np.dstack((output*255, output*255, output*255)) #Converts output to n x m x 3 greyscale image
    return grey_output.astype(int)

