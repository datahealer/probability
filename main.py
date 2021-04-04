# If two dice are rolled 1,000,000 times, what is the probability of getting sum of numbers greater than 7?
import numpy as np
n=1000000 #number of times dice is rolled
die1= np.random.randint(1,7,n)
die2= np.random.randint(1,7,n)
die_sum = die1+die2
result=sum(die_sum>7)
print('Result is: ', result)

