import numpy

def prime_factor(n):
    valor_inic = n
    num_prime = []
    p_f = []
    while int(n) not in num_prime or int(n) != 1.0:
        if int(n) in num_prime or int(n) == 1:
            break
        loop = True
        while loop:
            for c in num_prime:
                if numpy.prod(p_f) == valor_inic:
                    continue
                s = int(0)
                while s == int(s):
                    s = n / c
                    if s == int(s):
                        n = s
                        p_f.append(c)
            if int(n) in num_prime or int(n) == 1:
                loop = False
    return p_f

print(prime_factor(600851475143))





