import numpy as np
import pandas as pd

list1 = [1,2,3,4,5]
numpy1 = np.array((1,2,3,4,5), dtype=int)
dictionary1 = {"one":1, "two":2, "three":3, "four":4, "five":5}

print(pd.Series(list1, index=["one","two","three","four","five"]), end="\n\n")
print(pd.Series(numpy1, index=["one","two","three","four","five"]), end="\n\n")
print(pd.Series(dictionary1, index=["five","four","three","two","one"]))