import numpy as np
import matplotlib.pyplot as plt

a_list = np.arange(5,16)
print ("q1:", a_list) #question 1

b_list = np.linspace(0,23,7)
print ("q2:", b_list) #question 2, 7 evenly spaced numbers

x = np.arange(-1, 1, 1); # Part 2 exercise 3
plt.hist(x, bins = 20)
plt.show() # Part 2 exercise 4

# outputs random value in a 1x10 array
c = np.random.randint(1, 20, (1, 10))
# outputs random value in a 1x10 array
d = np.random.randint(1, 20, (1, 10)) 

print("q3:", c)
print("q4:", d)

# subtracting both the vectors and applying linear algebra 
dist = np.linalg.norm(d-c)

# printing Euclidean distance
print("q5:", dist)

