# 1. 소수여부를 판단한다.
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2. 2,000,000 이하의 Prime 수를 찾는다.
NUM = 2000000
prime_number = 2
prime_number_list = [2]
Sum_of_Prime_number = 0

while prime_number < NUM:
    if isPrime(prime_number):
        prime_number_list.append(prime_number)
    prime_number += 1
print(prime_number_list)

for n in prime_number_list:
    Sum_of_Prime_number += n