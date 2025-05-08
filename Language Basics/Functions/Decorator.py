def greet(func):
    def new_func():
        print("Hello! Nice to meet you.")
        func()
        print("Bye! Nice day.")
    return new_func()

@greet
def individual():
    print("Hi, Sir.")
individual()

def group():
    print("Hi, Team.")
greet(group())()