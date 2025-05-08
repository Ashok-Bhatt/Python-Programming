import matplotlib.pyplot as plt

labels = ["Chemistry","Physics","Maths","English","Computer"]
values = [70, 78, 82, 54, 57]

bars = plt.bar(labels, values)

# Another way:   bars[0].set_hatch("/")
patterns = ["o","*","-","+","/"]
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.show()