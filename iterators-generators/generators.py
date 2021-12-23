import os
import sys
import time
import random
import resource
# import psutil
# from pympler import summary, muppy


#  Utilities
def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

def memory_usage_resource():
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem


# Example 1
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])
print(my_nums.__next__())  
#OR 
print(next(my_nums))


# Example 2
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)

for num in my_nums:
    print(num)


# Example 3
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (After) : {}Mb'.format(memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))



# Example 4
list1 = [i for i in range(10000)]
print(sum(list1))
print(sys.getsizeof(list1), 'Bytes')

list2 = (i for i in range(10000))
print(sum(list2))
print(sys.getsizeof(list2), 'Bytes')