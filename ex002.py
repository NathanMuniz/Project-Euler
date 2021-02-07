fib_numbers = [1, 2]
fib_numbers_par = []
while fib_numbers[-1] < 4000000:
    fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

for c in fib_numbers:
    if c % 2 == 0:
        fib_numbers_par.append(c)

print(fib_numbers)
print(sum(fib_numbers_par))
