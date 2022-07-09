r = 1
b = 3
sum_r = 1
sum_b = 3
while sum_b - sum_r != 28:
    r = r + 4
    b = b + 4
    sum_r += 4
    sum_b += 4
print(sum_b+sum_r)