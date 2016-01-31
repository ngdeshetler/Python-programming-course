#Problem set 1
#Natalie De Shetler

#I've updated this a little bit from the one i showed in class.  I added comments, and I use boolean True/False for the prime test

from math import * #import math functions

#import math

n_s=[100,500,1000,5000] #list of all Ns to be used for problem 2
sum_logs=[0] * len(n_s) #pre-allocates a list that will hold the sums of the logs of the prime numbers
ratio_primeLog=[0] * len(n_s)
n_th=max(n_s); #find the max value in list n_s, so that the prime numbers only have to be calculated one
odds=3; 
primes=[2]; #starts the list of primes with 2 in the first, aka 0, position
log_primes=[log(2)];
while len(primes) < n_th: 
    is_prime=True; #for every odd number we assume that it is prime, then we check to see if it is not
    k=0;  
    while primes[k] <= sqrt(odds): #this will move throught the prime list until the prime number is greater than the square root of the odd number
        k +=1;
    for n in range(0, k): #this checks the odd number against every prime number less or equal to its square root
        if odds % primes[n] == 0:
            is_prime=False; 
            break #once found to be not prime, doesnt need to keep checking
    if is_prime: #if its prime, add to list
        primes.append(odds);
        log_primes.append(log(odds)); #also adds the log of the prime for part 2
    odds += 2;

for f in range(len(n_s)): #for all the possible Ns I made above
    k=0;
    while primes[k] < n_s[f]:#finds the largest prime less than N
        k +=1
    sum_logs[f]=sum(log_primes[0:k-1]) #calculates and saves the sum of the logs that are less than that N
    ratio_primeLog[f]=sum_logs[f]/n_s[f] #same for the ratio

#This just prints out all my answers fancy like
print('\n-Here are the answers to problem set 1-')
print('\nProblem 1:\nThe 1000th prime number is ' + str(primes[999]))
print('\nProblem 2:\nWhen we set Ns to the following:')
print(n_s)
print('the sum of the logs of all prime numbers less than that N are:')
print(sum_logs)
print('and the ratio between the sum of the logs of all prime numbers less than that N and N are:')
print(ratio_primeLog)
