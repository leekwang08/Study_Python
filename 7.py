def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_check = 1
n = 3
turn = 1

while prime_check < 10001:

    if isPrime(n):
        prime_check += 1
        result = n
        print("%d    %d    %d" % (turn, prime_check, result))
    n += 1
    turn += 1