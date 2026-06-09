class Grader():
    def __init__(self):
        self.name = self.getName()
        self.marks = self.getMarks()
        self.avg = self.getAvg()
        self.returnGrade()
        
    def getName(self):
        name = input("Enter student name: ")
        return name
    
    def getMarks(self):
        marks = []
        for i in range(3):
            marks.append(float(input("Enter grade " + str(i+1) + ": ")))
        return marks
    
    def getAvg(self):
        total = 0
        for g in self.marks:
            total += g
        average = total / len(self.marks)
        return average
    
    def returnGrade(self):
        print("Student: " + self.name)
        print("Grades: " + str(self.marks))
        print("Average: " + str(round(self.avg, 1)))
        if self.avg >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

g = Grader()
