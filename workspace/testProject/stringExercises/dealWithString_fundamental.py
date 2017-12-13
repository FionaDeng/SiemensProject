"""
涉及：字符串、函数
1、基础：
循环获取用户的输入的字符串，按照下面的处理规则处理后，输出另一个字符串。
规则：
a) 如果字符串长度小于等于5，则反向输出。如，input ："abcde" -> output: "edcba"
b) 如果字符串长度小于等于10，则将前5个字符串替换成hello， 如，input : "abcdefgh" -> output: "hellofgh"
c) 否则，输出index（索引值）为偶数的字符组成的字符串的最后5位。 如，input : "0a1b2c3d4f5g6h” -> output : "23456"
d）特别的，如果字符串为'quit'，则退出程序。
"""
var = 1
str = ''
while var == 1:
    user_input = input("Enter:")
    if user_input.__eq__('quit'):
        print('End!')
        break
    else:
        if user_input.__len__() <= 5:
            print(user_input[::-1])
        elif user_input.__len__() <= 10:
            print('hello' + user_input[5:])  # replace ?
        else:
            for i in range(len(user_input)):
                if (i % 2) == 0:
                    str += user_input[i]
            print(str[str.__len__()-5:])
