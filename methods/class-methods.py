# Key Takeaways
# Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.


class MyClass:

    @classmethod
    def classmethod(cls):
        return 'class method called', cls


obj = MyClass()
print(obj.classmethod())

print(MyClass.classmethod())
