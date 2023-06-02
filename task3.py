class Student:

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
        
stu = Student()
stu.setName('Eren')
print(stu.getName())
stu.setRollNumber(100)
print(stu.getRollNumber())