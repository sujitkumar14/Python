class Employee:
    raise_amt = 1.04
    def __init__(self,name):
        self.name = name
    def names(self):
        return self.name
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

class Developer(Employee):
    def __init__(self,name):
        Employee.__init__(self,name)

if __name__=="__main__":
    emp = Employee('sujeet')
    dev = Developer('manoj')
    Employee.set_raise_amt(1.05)
    print emp.name
    print emp.names()
    print emp.raise_amt
    print Employee.raise_amt
    print dev.names()
    
#Instance variables and class variables 
