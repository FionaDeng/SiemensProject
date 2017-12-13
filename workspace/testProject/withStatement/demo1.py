__author__ = 'FionaDeng'

class sample:
    def __enter__(self):
        print("__enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("__exit__()")

def get_sample():
        return sample()

with get_sample() as sample:
    print("sample:",sample)