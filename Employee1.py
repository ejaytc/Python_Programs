#Python Object oriented programming exercise


class Employee:


    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print( "Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:" , self.name, ", Salary:", self.salary)




if __name__ == "__main__":
    #Create instances of class
    #This woul create first object of Employee class"
    emp1 = Employee("Zara", 2000)
    #This would create seond object of Employee class"
    emp2 = Employee("Manni", 5000)    


    #Accessing Attributes

    Employee.displayCount(emp1)
    Employee.displayCount(emp2)
    #or

    emp1.displayCount()
    emp2.displayCount()

    print("Total Employee %d" % Employee.empCount)
