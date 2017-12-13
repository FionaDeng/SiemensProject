__author__ = 'FionaDeng'

with open("./tmp/foo.txt") as file:
    data = file.read()

# just like it as below
# one
file = open("./tmp/foo.txt")
data = file.read()
file.close()

# two
file = open("./tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()
