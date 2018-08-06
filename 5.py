NUM = 20
prime_numbers = [2]
dic = {}
result = 1

# 소수 찾기
for num in range(3, NUM+1):
    isPrime = 0
    for i in range(2, num):
        if num % i == 0:
            isPrime += 1
    if isPrime == 0:
        prime_numbers.append(num)

# 소수별 최대배수 구하기
for i in prime_numbers:
    i_no_list = []
    for n in range(2, 20):
        i_no = 0
        while n % i == 0:
            n /= i
            i_no += 1
        i_no_list.append(i_no)

    dic[i] = max(i_no_list)

# 소수1^MAX_NO*소수2^MAX*....
for prime_number, n in dic.items():
    result *= (prime_number**n)

print(result)












# number = 20
# temp_numbers = []
# result = 1
#
# for num in range(2, number+1):
#     n = 2
#     while num > 1:
#         while num % n ==0:
#             num /= n
#             temp_numbers.append(n)
#         n += 1
#
# least_common_multiple_numbers = list(set(temp_numbers))
# print(least_common_multiple_numbers)
# for num in least_common_multiple_numbers:
#     result *= num
#
# print(result)