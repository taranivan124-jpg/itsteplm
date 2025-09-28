list = [1, 2, 4, 8, 16]

# for j in range(10):
#     for i in list:
#         print(i)

iterr = iter(list)
# print(next(iterr))
# print(next(iterr))
# print(next(iterr))
#
# for i in iterr:
#     print(i)


class Counter:
    def __init__(self, max):
        self.count = 0
        self.max = max
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        self.count += 1
        if self.count > self.max:
            raise StopIteration
        return self.count

counter = Counter(5)
# print(counter.__next__())
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# # print(next(counter))



def my_generator(number, max_num):
    for i in range(max_num):
        yield number**i

res = my_generator(2,10)
# print(res)
# for i in res:
#     print(i)

class Callobj:
    def __init__(self, name):
        print("My name is", name)
    def __call__(self, name):
        print(name)

# my_call = Callobj("Bob")
#
# my_call("Ann")

def decorator(func):
    print("start")
    func()
    print("end")



def my_func():
    print("щось там бла бла бла функція")

my = decorator(my_func)
decorator(my_func)