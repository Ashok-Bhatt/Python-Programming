import os
print(os.getcwd)

print("#"*100 + "\n")
print(os.environ["PATH"])
print("\n" + "#"*100)

import sys
print(sys.version)
print(sys.path)
print(sys.modules)
txt="My name is AShok Bhatt."
print(sys.getrefcount(txt))