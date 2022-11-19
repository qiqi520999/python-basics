"""
Nhập vào hai biến num1 và num2
Tính tổng, hiệu, tích, thương, chia nguyên, chia dư, 
lũy thừa giá trị của 2 biến
"""

"""
b1: input/output
b2: logic
b3: print
"""

num1 = float(input('num1 = ')) # Shift + Alt + Bottom Arrow
num2 = float(input('num2 = '))

total = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2
# //
int_div = num1 // num2
remainder = num1 % num2

exp = num1 ** num2

# x + y = t
# Ctrl + Alt + N
print(num1, '+', num2, '=', total)
print(num1, '-', num2, '=', sub)
print(num1, '*', num2, '=', mul)
print(num1, '/', num2, '=', div)
print(num1, '//', num2, '=', int_div)
print(num1, '%', num2, '=', remainder)
print(num1, '^', num2, '=', exp)

"""
- input function => string
- operator: +, -, *, / (float), // (int), **, %
"""
