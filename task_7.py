def digit_root(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
