import sys

data = ''

with open(sys.argv[1]) as f:
	for n in f:
		data += n 
		#print(n)

#print(data)

nums = [int(i) for i in data.split(' ')]
es = [0.75 * nums[3], 0.5 * nums[4]]
for i in range(3):
    es.append(nums[i])
print(sum(es) * 2)