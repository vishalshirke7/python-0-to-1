# Key Takeaways
# Instance methods need a class instance and can access the instance through self.


class MyClass:
    def method(self):
        return 'instance method called', self

obj = MyClass()
print(obj.method())

print(MyClass.method(obj))