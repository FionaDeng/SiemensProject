"""
2、进阶：
将上述规则定义成函数hand_str, 有参数两个word，is_strip_space， word为待处理的字符串str，is_strip_space为bool值，默认值为True，
输出一个处理好的新字符串。
若is_strip_space为False则按上述规则处理，
若is_strip_space为True，则先将word所有的空格均去掉，再按上述规则。(提示：字符串转列表，处理完后再转换成字符串)
"""

def hand_str(word,is_strip_space):
    str = ''
    if is_strip_space == False:
        if word.__len__() <= 5:
            return (word[::-1])
        elif word.__len__() <= 10:
            return ('hello' + word[5:])
        else:
            for i in range(len(word)):
                if (i % 2) == 0:
                    str += word[i]
            return (str[str.__len__()-5:])
    else:
        list1 = word.split(' ')
        word = ''.join(list1)
        is_strip_space = False
        return (hand_str(word,is_strip_space))


var = 1
while var == 1:
    str_input = input('Enter: ')
    if str_input == 'quit':
        break
    else:
        print(hand_str(str_input, True))



