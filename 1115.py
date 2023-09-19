from threading import Event, Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.c = Barrier(2)  
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.c.wait()  
    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.c.wait()  
            printBar()
            self.c.reset()  