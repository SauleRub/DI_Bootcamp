# exercise_one.py

import func
print(func.sum_numbers(3, 7))

from func import sum_numbers
print(sum_numbers(5, 8))

from func import sum_numbers as sn
print(sn(2, 4))

import func as f
print(f.sum_numbers(10, 20))