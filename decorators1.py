import decorators as dc

@dc.repeat
def say_whee():
    print("Whee!")

@dc.repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

say_whee()
print("\n")
greet=dc.repeat(num_times=3)
print('\n')

class TimeWaster:
    @dc.debug
    def __init__(self, max_num):
        self.max_num = max_num

    @dc.timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
            
tw = TimeWaster(1000)
tw.waste_time(999)
print('\n')

#Using decorator stacking
@dc.debug
@dc.do_twice
def greet1(name):
    print(f"Hello {name}")

greet1('lilly')
print('\n')

#notice the difference
@dc.do_twice
@dc.debug
def greet2(name):
    print(f"Hello {name}")
        
greet2('lilly')
print('\n')

@dc.count_calls
def say_hurray():
    print("Hurray!")
    
say_hurray()
say_hurray()
print(f'{repr(say_hurray.__name__)} called {say_hurray.num_calls} times\n')

# say_Cheese=CountCalls(say_cheese)
# say_Cheese is a class object now
# calling it like a function would call the __call__ method
@dc.CountCalls
def say_cheese():
    print("Cheese!")

say_cheese()
say_cheese()
print(f'number of times{say_cheese.__name__} called : {say_cheese.num_calls} \n')

@dc.slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
        
countdown(4)