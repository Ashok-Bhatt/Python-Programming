import os
import time

def printPyramid(string : str) -> None:

    start : int = 0
    length : int = 1
    string_length : int = len(string)

    while start < string_length:
        if start+length > string_length:
            print(string[start:string_length] + "*"*(start+length-string_length))
        else:
            print(string[start:start+length])
        start = start + length
        length = length + 1


def oneLinerPyramid(string : str) -> None:
    print([(i,sum(range(i+1))) for i in range(5)])



def main() -> None:

    oneLinerPyramid("Ashok")

""" 
    sample_string : str = "#"*105
    for i in range(len(sample_string)):
        os.system("cls")
        printPyramid(sample_string[0:i+1])
        time.sleep(0.05)
 """

if __name__ == "__main__":
    main()