import time
import timeit 
from random import randint
import os
from functools import wraps
import logging 

# https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk 
# https://www.geeksforgeeks.org/how-to-get-the-current-username-in-python/ 
# https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string
# https://www.w3schools.com/python/python_file_write.asp 


def log(func):
    def wrapper(*args, **kwargs) :
        username = os.getlogin() 
        func_name = func.__name__.replace('_', ' ').title() 
        prefix = 'ms'
        # Self-Timeit

        f = open("machine.log", "a")

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
       
        end_time = time.perf_counter()
        time_exec = end_time - start_time 
        if time_exec < 0.001 : 
            time_exec = time_exec * 10000
        else :
            prefix = 's'
        ret=f"({username})Running: {func_name:18} [exec-time = {time_exec:.3f}{prefix}]\n" 
        f.write(ret) 
        return result 
    return wrapper



class CoffeeMachine():
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)