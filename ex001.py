#som_a = som_b = 0
#for c in range(0, 1000):
#    if c % 3 == 0 or c % 5 ==0:
#        som_a += c
#        print(f"{c}", end=" ")
#print(f"{som_a}")
#print(f"{som_b}")
#print(f"{som_a + som_b}")

num_prime = []
mult = 0
for c in range(2, 10):
    for count in range(2, c):
        if (c % count == 0):
            mult += 1
        if mult <= 2:
            num_prime.append(c)

print(num_prime)