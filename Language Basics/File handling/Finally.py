num=input("Enter the number:")
try:
    print(int(num))
except Exception as e:
    print(e)
# Statements written in finally block will be executed for sure
# below statement is equivalent to : print("My impotant code.") as finally keyword was not important
finally:
    print("My important code.")

def final(num):
    try:
        print(int(num))
        return 1
    except Exception as e:
        print(e)
        return 0
    # Statements written in finally keyword is definately executed even if it has returned some values
    # It will be executed before return statement 
    finally:
        print("My important code.")
num1=input("Enter the number:")
print(final(num1))