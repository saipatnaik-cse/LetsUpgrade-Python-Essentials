#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Write a python Function for finding is a given number prime or not and do Unit Testing on it using
# PyLint and Unittest Library

# In[3]:


def isPrime(n):
    
    '''
    Hey I am testing pyLint of this code
    '''

    if (n <= 1):
        # not a prime number
        print("Not a Prime Number")
    if (n <= 3):
        # is a prime number
        print("Is a Prime Number")
  
    # This is checked so that we can skip 
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        print("Not a Prime Number")
  
    i = 5
    while(i * i <= n):
        # not a prime number
        if (n % i == 0 or n % (i + 2) == 0):
            print("Not a Prime Number")
        i = i + 6
  
    print("Prime Number")
    
isPrime(23)


# In[ ]:




