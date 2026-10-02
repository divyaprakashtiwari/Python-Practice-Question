# Level 2 - Q6: Prime Function
# Write a function to check whether a number is prime.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(is_prime(num))
