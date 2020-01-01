def sum_sqaure_difference():
  sum_of_squares = 0
  square_of_sum = 0
  acc = 0
  for i in range(1, 101):
    square_each_num = i ** 2
    acc += i
    sum_of_squares += square_each_num
  square_of_sum += acc ** 2
  answer = square_of_sum - sum_of_squares
  return answer

print(sum_sqaure_difference())