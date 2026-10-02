# Level 3 - Q7: Prime Numbers Using List Comprehension & Helper Function
# Use list comprehension and a helper function to create a list containing only prime numbers.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Find primes up to: "))
primes = [n for n in range(1, limit + 1) if is_prime(n)]
print(primes)
