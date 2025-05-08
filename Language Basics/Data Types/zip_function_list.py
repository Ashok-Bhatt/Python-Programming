names = ["Ashok","Aman","Ashwin","Adarsh"]
marks = [78,70,89,60]
subjects = ["Physics","Maths","Biology","Chemistry"]

for name,mark,subject in zip(names,marks,subjects):
    print(f"{name} has scored {mark} out of 100 in {subject}.")