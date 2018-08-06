# 특정 숫자 이하의 소수를 어떻게 찾을까?
number = 600851475143
num, prime_num_check = 2, 0
prime_num_list = []

while num <= number:

    if number % num == 0:
        number = number / num

        for i in range(2, int(num/2)+1):
            if num % i == 0:
                prime_num_check += 1
                break
            if prime_num_check == 0:
                prime_num_list.append(num)

    num += 1

prime_num_list = list(set(prime_num_list))
prime_num_list.sort()

result = prime_num_list[-1]
print(result)