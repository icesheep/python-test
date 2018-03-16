import math
def is_palindrome(n):
    n_str = str(n)
    n_len = len(n_str)
    center = math.floor(n_len/2)
    i = 0
    while i < center:
        if n_str[i] != n_str[n_len-1-i]:
            return False
        i = i+1
    return True
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')