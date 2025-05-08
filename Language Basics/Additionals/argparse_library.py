import argparse

parser = argparse.ArgumentParser(description="This program will calculate the sum of first n natural number")
parser.add_argument("-n", default=1, help="n will be the number upto which we will calculate the sum of natural numbers from 1.", type=int)
args = parser.parse_args()

if args.n < 0:
    raise ValueError("n must be whole number.")
else:
    n = args.n
    print(n*(n+1)//2)