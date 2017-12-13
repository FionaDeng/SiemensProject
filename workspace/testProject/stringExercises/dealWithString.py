import unittest
import sys


def hand_str(word,is_strip_space=True):
    if word.lower() == 'quit':
        print()
    else:
        if not is_strip_space:
            if len(word) <= 5:
                return word[::-1]
            elif len(word) <= 10:
                return 'hello' + word[5:]
            else:
                return word[::2][-5:]
                # Note: other methods are as follows
                # str = ''
                # for i in range(len(word)):
                #     if (i % 2) == 0:
                #         str += word[i]
                # return str[len(str) - 5:]
        else:
            list1 = word.split(' ')
            word = ''.join(list1)
            is_strip_space = False
            return (hand_str(word, is_strip_space))

class handleStr(unittest.TestCase):
    def boundry(self):
        self.assertEqual(hand_str('abcdefgh'),'hellofg')


if __name__ == 'main':
    unittest.main(verbosity=1)


