# Level 2 - Q2: Prime Numbers Using List Comprehension
# Generate a list containing only prime numbers between 1 and 100 using list comprehension.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(1, 101) if is_prime(x)]
print(primes)
