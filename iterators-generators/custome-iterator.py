# MyRange is a Iterable because we are able to run for loop over it
# It is also a iterator because it has next method in it


class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    # This class makes it a iterable
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)

# generators
def my_range(start, end):
    current = start
    while current < start + 100:
        yield current
        current += 1

nums_g = my_range(1, 100)
for num in nums_g:
    print(num)