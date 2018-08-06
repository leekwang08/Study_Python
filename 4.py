# palindromic number 만드는 방법
number = 999
num = 0
palindromic_number_list = []
numbers_list = []

for i in range(0, 900):
    left_number = number - i
    temp_list = list(str(left_number))
    temp_list.reverse()
    right_number = "".join(temp_list)
    palindromic_number = str(left_number) + right_number
    palindromic_number_list.append(int(palindromic_number))

for i in range(100, 1000):
    for k in range(100, 1000):
        numbers_list.append(i*k)

for pal_number in palindromic_number_list:
    for num in numbers_list:
        if pal_number == num:
            print(pal_number)
            exit(1)

#     for i in range(100, 1000):
#         for k in range(i, 1000):
#             if i * k == int(palindromic_number):
#                 palindromic_number_list.append(palindromic_number)
# print(palindromic_number_list)



    # for num in range(100, 1000):
    #     if int(palindromic_number) % num == 0:
    #         if int(palindromic_number) / num > 100:
    #             palindromic_number_list.append(palindromic_number)
    #             break

                # result_a = num
                # result_b = int(palindromic_number) / num

# print("A:%d  B:%d  Palindromic Number:%d" % (result_a, result_b, result_a*result_b))




