# 제곱근이 정수인지 판단한다.
def is_int(x):
    if x == int(x):
        return True
    else:
        return False

# 1.  NUM 숫자 안에서 제곱근이 정수인 수를 리스트화 한다.
NUM = 1000
NUM_SQUARE = NUM**2
numbers = []
abc_numbers = []
result_a, result_b, result_c = 0, 0, 0

for n in range(1, NUM_SQUARE+1):
    if is_int(n**0.5):
        numbers.append(n)
print(numbers)
# 2. 제곱근이 정수인 리스트 값에 임의의 a를 꺼내고 b를 꺼내고 c를 꺼낸다.
for i in range(0, len(numbers)):
    a2 = numbers[i]
    for k in range(i+1, len(numbers)):
        b2 = numbers[k]
        c2 = a2 + b2
        try:
            if (numbers.index(c2) > 0) and (a2 < b2) and (b2 < c2):
                temp_list = [a2, b2, c2]
                abc_numbers.append(temp_list)
        except:
            pass
print(abc_numbers)
# 3. 찾은 abc 리스트의 각 값의 제곱근 값을 구한다.
for i in range(0, len(abc_numbers)):
    if abc_numbers[i][0]**0.5 + abc_numbers[i][1]**0.5 + abc_numbers[i][2]**0.5 == NUM:
        result_a = int(abc_numbers[i][0]**0.5)
        result_b = int(abc_numbers[i][1]**0.5)
        result_c = int(abc_numbers[i][2]**0.5)
print(result_a*result_b*result_c)