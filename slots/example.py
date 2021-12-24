class TestClass(object):


    __slots__ = ("a", "b", "c")


    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


if __name__ == "__main__":


    instance = TestClass()


    print(instance.__slots__)


    print(instance.a)
    print(instance.b)
    print(instance.c)    