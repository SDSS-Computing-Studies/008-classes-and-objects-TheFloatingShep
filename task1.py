#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name = ""
    code = ""
    grade = int()
    courses = []
    grades = []

    def getCourses(self, lis):
        self.courses = lis

    def getGrades(self, *arg):
        gr = []
        for x in range(len(arg)):
            gr.append(arg[x])
        self.grades = gr

    def __init__(self, name, code, grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.code = code
        self.grade = grade

    def __del__(self):
        pass

    def average(self):
        av = 0
        for x in range(len(self.grades)):
            av += self.grades[x]
        return round(av / len(self.grades), 1)

    def getHonorRoll(self):
        lis = self.grades
        lis.sort(reverse = True)
        hr = 0
        for x in range(5):
            hr += lis[x]
        ans = hr / 5
        if ans >= 86:
            return True
        else:
            return False
    
    def showCourses(self):
        print(self.courses)

    def showGrade(self, x):
        print(self.courses[x] + " " + self.grades[x])


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( 91, 94, 87, 99, 82, 100, 73)

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( 71, 98, 93, 95, 68, 81, 71)

main()