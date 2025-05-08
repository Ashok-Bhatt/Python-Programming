def mean(*args):
    """
    The mean function helps to find the mean of numbers specified in the arguments
    Mean function can take as many arguments as it can take
    """
    sum=0
    for i in args:
        sum+=i
    return sum/len(args)

print("The mean of given arrguments is:",mean(3,5,6))