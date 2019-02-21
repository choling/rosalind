adults = 0
children = 1

count = 1
newadults = 0

n = 28 # number of iterations (months)
k = 4 # number of times each pair 

while (count < n):
    newadults = adults + children
    children = adults * k
    adults = newadults
    count = count + 1
    
print (adults + children)

