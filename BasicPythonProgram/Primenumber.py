noprimes = []
for i in range(2, 8):
    for j in range(2 * i, 50, i):
        noprimes.append(j)
        
print noprimes
        
prime =[x for x in range(2,50) if x not in noprimes]

print prime
