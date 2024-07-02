class Employee:
    raise_amount = 0.04
    nb_of_emps = 0
    
    def __init__(self, firstName:str, lastName:str, salary:float):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.email = f"{self.firstName}.{self.lastName}@company.org"
        Employee.nb_of_emps +=1
    
    def fullname(self)->str:
        return f"{self.fistName} {self.lastName}"
    
    def salary_update(self, salary:float)->float:
        self.salary = self.salary*(1 + Employee.raise_amount)
    
    @classmethod
    def set_raise_amt(cls,raise_amt:float):
        cls.raise_amount= raise_amt
        
    @classmethod
    def from_string(cls, emp:str):
        list = emp.split("-")
        return cls(list[0], list[1], float(list[2]))
    
    def __add__(self, self1):
        return self.salary + self1.salary 
    
    def day_work(day:str)->bool:
        list = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
        return day in list
class Developer(Employee):
    raise_amount = 0.1
    def __init__(self, firstName:str, lastName:str, salary:float,  prog_lang:str):
        super().__init__(firstName, lastName, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, firstName: str, lastName: str, salary: float, employee:list=None):
        super().__init__(firstName, lastName, salary)
        self.employee = employee if employee != None else None
    
    def add_emp(self, employer:Employee):
        self.employee.append(employer)
    
    def remove_emp(self, employer:Employee):
        self.employee.remove(employer)
    
    def print_emps(self):
        for emp in self.employee:
            print(emp.fullname())

if __name__ == '__main__':
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Jane", "Doe", 100000)
    emp3 = Employee("Jane", "Doe", 100000)
    emp4 = Employee("Jane", "Doe", 100000)
    emp5 = Employee("Jane", "Doe", 100000)
    emp6 = Employee("Jane", "Doe", 100000)
    emp7 = Employee("Jane", "Doe", 100000)
    emp8 = Employee("Jane", "Doe", 100000)
    print(emp1.__add__(emp2)) 
    print(emp1.salary_update(emp1.salary))
    print(Employee.nb_of_emps)
    print((Employee.from_string("John-Doe-70000")).salary)  
    print(emp1+emp2) 
