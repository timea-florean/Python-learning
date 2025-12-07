#example of creating and using an iterator
class CountDown:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=0:
            raise StopIteration
        else:
            num=self.current
            self.current-=1
            return num
#using the iterator
counter=CountDown(3)
for num in counter:
    print(num)

#example of a generator function
def reverse_countdown(n):
    while n>0:
        yield n
        n-=1
#using the generator
for i in reverse_countdown(3):
    print(i)

#decorators
#example of a simple decorator

def debug(func):
    def wrapper( *args, **kwargs):
        result=func(*args,**kwargs)
        print(f"Function {func.__name__!r} returned {result!r}")
        return result
    return wrapper
@debug
def add(a,b):
    return a+b
print(add(5,3))

#context managers

#example of creating a context manager using a class;
class ManagedFile:
    def __init__(self,filename):
        self.filename=filename
        self.file=None
    def __enter__(self):
        self.file=open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
#using the context manager
with ManagedFile('hello.txt')as f:
    f.write('Hello, world!')
    f.write('This file is managed automatically')
print("File 'hello.txt' created and closed successfully")

#example
from contextlib import contextmanager
@contextmanager
def managed_file(filename):
    try:
        f=open(filename, 'a')
        yield f
    finally:
        f.close()
#using the generator-based context manager
with managed_file('hello.txt')as f:
    f.write("Hello, again!")
    f.write('Generators make this easy!')