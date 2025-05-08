import time
import sys

class student:

    def __init__(self,enrollmentNo,discipline,gotmarks,maxmarks=500,passpercentage=35):
        self.eroll = enrollmentNo
        self.dis = discipline
        self.gotmarks = gotmarks
        self.mmark = maxmarks
        self.passper = passpercentage

    def percentage(self):
        return (self.gotmarks / self.mmark) * 100
    
    def result(self):
        if self.percentage() >= self.passper:
            return "pass"
        else:
            return "fail"
 
class graduate(student):
    def __init__(self, enrollmentNo, discipline, gotmarks, maxmarks=600, passpercentage=40):
        super().__init__(enrollmentNo, discipline, gotmarks, maxmarks, passpercentage)

class postgraduate(student):
    def __init__(self, enrollmentNo, discipline, gotmarks, maxmarks=400, passpercentage=50):
        super().__init__(enrollmentNo, discipline, gotmarks, maxmarks, passpercentage)

s = student(123,"DMP",455)
print(round(s.percentage(),2))
print(s.result())

g = graduate(456,"python",512)
p = postgraduate(789,"java", 356)
print(round(g.percentage(),2))
print(g.result())
print(round(p.percentage(),2))
print(p.result())

start_time = time.time()
s = student(123, "Computer Science", 455)
g = graduate(456, "Computer Science", 512)
p = postgraduate(789, "Data Science", 356)
print("Time taken: ", time.time() - start_time)

print("Space complexity:", sys.getsizeof(s) + sys.getsizeof(g) + sys.getsizeof(p))