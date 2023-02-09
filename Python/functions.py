''' Write a python function that can add any number of iterables when passed as parameters to it. Include appropriate docstring for the function. 
Show the execution with various cases.'''

def sum1(*args):
    """
    This function takes any number of iterables as parameters or input and returns the sum of all elements in the iterables
    """
    r = 0
    for i in args:
        r = r + i
    return r

print(sum1(1,2,3,4,5))

''' Given a sequence of n values x1, x2, xn and a window size k>0, the k- th moving average of the given sequence is defined as follows:
The moving average sequence has n-k+1 elements as shown below. The
moving averages with k=4 of a ten-value sequence (n=10) '''

l1 = [3,5,7,2,8,10,11,65,72,81,99,100,150]
k = 3
num = len(l1) - k + 1
for i in range(num):
    avg = 0
    sum1 = 0
    for j in l1:
        sum1 = sum(l1[i:i+k])
        avg = round(sum1/k)
       
    print(avg)
    
    ''' 3rd Q '''
    
def vandermonde_matrix(array, p, ascending=False):
if not ascending:
    return [[element**(p-i-1) for i in range(p)] for element in array]
else:
    return [[element**i for i in range(p)] for element in array]


array = [1, 2, 3]

p = 3

result = vandermonde_matrix(array, p)
print(result)

result = vandermonde_matrix(array, p, True)
print(result)

