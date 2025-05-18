import module as m
from math import sqrt as s, pi as p  # changing name as my requirement

# if we want to import specific function, write as
from module import add, subtract

print(m.multiply(3, 5))
print(m.divide(7, 5))


print(add(3, 8))
print(subtract(4, 3))


print(f"Square root of given number is: {s(16)}")
print(f"The value of pi is: {p}")
