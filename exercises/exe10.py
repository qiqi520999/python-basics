"""
Hỏi tên người dùng, sau đó chào người dùng, 
sử dụng tên của họ như một phần của lời chào. 
Tên phải ở trong dạng tiêu đề và 
không được bao quanh bởi bất kỳ khoảng trắng thừa nào.

Ví dụ: nếu người dùng nhập "lewis ", 
đầu ra của bạn sẽ giống như thế này:
'Hello, Lewis!'
"""
name = input('Enter your name: ')
"""
'john doe'
title: 'John Doe'
"""
result = name.title()
result1 = result.strip() # remove space+, \n+, \t+ at start or end of string
print(result1)
