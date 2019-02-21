import sys

#Fn = F(n-1)+F(n-2)-F(n-m-1)

n = int(input("remain after nth_month:\n"))
m = int(input("live for m_months:\n"))

bunnies = [1, 1]                                                               
months = 2   
count = 0                                                                  
while months < n:                                                              
    if months < m:                                                             
        bunnies.append(bunnies[-2] + bunnies[-1])                              
    elif months == m or count == m + 1:                                        
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
    else:                                                                      
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(                  
            m + 1)])                                                           
    months += 1                                                                
print(bunnies[-1]) 
