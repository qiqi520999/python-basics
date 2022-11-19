"""
Tính và in ra chu vi và diện tích của một hình tròn bán kính 5 đơn vị
Note: lấy pi = 3.14
"""
"""
input: r = 5
output: cv, dt

logic:
cv = 2 x pi x r
dt = pi x r ^ 2
"""

PI = 3.14
r = 5

cv = 2 * PI * r
dt = PI * r ** 2

print(f"Chu vi: {cv}")
print(f"Dien tich: {dt}")
