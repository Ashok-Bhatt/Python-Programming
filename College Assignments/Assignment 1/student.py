from abc import ABC, abstractmethod

class Student(ABC):
    maxMarks = 600
    passPercentage = 35

    def __init__(self, enrollmentNo, discipline, gotMarks):
        self.enrollmentNo = enrollmentNo
        self.discipline = discipline
        self.gotMarks = gotMarks

    @abstractmethod
    def percentage(self):
        pass

    @abstractmethod
    def result(self):
        pass

    def enrollment(self):
        return f"Your enrollment number is {self.enrollmentNo}."

class Graduate(Student):
    maxMarks = 600
    passPercentage = 40

    def percentage(self, gotMarks, maxMarks):
        return gotMarks*100/maxMarks
    
    def result(self, discipline, gotMarks, passPercentage, maxMarks):
        if (gotMarks*100/maxMarks>passPercentage and discipline==True):
            return True
        else:
            return False

class PostGraduate(Student):
    maxMarks = 400
    passPercentage = 50

    def percentage(self, gotMarks, maxMarks):
        return gotMarks*100/maxMarks
    
    def result(self, discipline, gotMarks, passPercentage, maxMarks):
        if (gotMarks*100/maxMarks>passPercentage and discipline==True):
            return True
        else:
            return False

graduate = Graduate("22C21007",True, 520)
print(graduate.enrollment())
print(f"You have scored {graduate.percentage()}%.")

if (graduate.result()==True):
    print("You are passed.")
else:
    print("You are failed.")