NUM = 1000
sum_of_square = 0
square_of_sum = 0
temp_sum, diff = 0, 0

for n in range(1, NUM+1):
    sum_of_square += n**2

for n in range(1, NUM+1):
    temp_sum += n
    square_of_sum = temp_sum**2

diff = square_of_sum - sum_of_square
print(diff)
