import threading

a = int(input("Enter any number:"))

def square():
    print(f"the square of number {a} is {a ** 2} ")
 
def cube():
    print(f"the cube of number {a} is {a ** 3}")

if __name__ == '__main__':
    thread1 = threading.Thread(target=square)
    thread2 = threading.Thread(target=cube)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('Done')