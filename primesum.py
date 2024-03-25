import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primesum():
    sum = 0
    for line in sys.stdin:
        num = int(line.strip())
        if is_prime(num):
            sum += num
    return sum

total = primesum()
print("The sum of the primes is", total, end=".")

