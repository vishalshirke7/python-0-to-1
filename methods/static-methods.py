# Key Takeaways
# Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
# Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.


class MyClass:

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.staticmethod())

print(MyClass.staticmethod())