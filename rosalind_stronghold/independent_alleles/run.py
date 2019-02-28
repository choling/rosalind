import sys
import math

file = open(sys.argv[1])
f = file.readline().rstrip()

data = []
for i in f:
	data.append(i)

#print(type(data[2]))

k_generation = int(data[0])
n_organism = int(data[2])

print(type(k_generation))

#k_generation = int(input("K =\n"))
#n_organism = int(input("N =\n"))

population = 2**k_generation

probability = 0

for i in range(n_organism, population+1):
	prob = (math.factorial(population)/(math.factorial(i)*math.factorial(population-i)))*(0.25**i)*(0.75**(population-i))
	probability += prob

print(round(probability,3))


