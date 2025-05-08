import threading

def print_numbers():
    for i in range(1, 11):
        print(i,end=" ")

def print_letters():
    for letter in 'abcdefghij':
        print(letter, end=" ")

if __name__ == '__main__':
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('Done')