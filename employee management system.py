class office:
    def __init__(self, name, eid):
        self.name = name
        self.eid = eid
        self.a = {}
        self.b = {}

    def department(self):#correct
        w  = int(input("Number of departments: "))
        for i in range(w):
            dep_id = int(input("Enter department id: "))
            dep_name = input("Department name: ")
            self.a[dep_name] = dep_id
            
        return self.a

    def add_emp(self): #correct
        v = int(input("Number of employees to be added: "))
        for i in range(v):
            ename= input("Enter Employee name: ")
            eeid = int(input("Enter Employee ID: "))
            edep = input("Which Department: ")
            level = input("Level of the emolyee(A,B,C,D): ")
            if level not in ("A", "B", "C", "D"):
                return("Level is wrong fix it")
                
            if edep in self.a:
                self.b[ename] = {"Id": eeid, "Dep": edep, "Level": level}
                print(self.b)
            else:
                return "wrong entry..."
        return ""
    def remove_emp(self): #issue resolved
        x = int(input("Numer of employees to be removed: "))
        for i in range(x):
            ename= input("Enter Employee name: ")
            eeid = int(input("Enter Employee ID: "))
            edep = input("Which Department: ")
            if edep in self.a:
                self.b[ename] = {"Id": eeid, "Dep": edep}
                del self.b[ename]
                print( self.b)
            else:
                return "wrong entry..."
        return ""

    def total_emp(self): #solved
        z = int(input("Choose:-\n 1. Total employee\n  2. Employee in each department\n "))
        if z == 1:
            return self.b
        elif z==2:
            edep = input("Which department: ")
            for emp_name, emp_info in self.b.items():
                if edep == emp_info["Dep"]:
                    print(emp_name, emp_info)
        return""


    def salary(self):
        for emp_name, emp_info in self.b.items():
            if emp_info["Level"] == "A":
                 print(f"salary of {emp_name}: 100000")
            elif emp_info["Level"] == "B":
                 print("salary of {emp_name}: 80000")
            elif emp_info["Level"] == "C":
                 print("salary of {emp_name}: 60000")
            elif emp_info["Level"] == "D":
                 print("salary of {emp_name}: 20000")
        return ""
         

user = input("User name: ")
user_id = input("User id: ")
a = office (user, user_id)
print("---Welcome---\n Now first task is to add departments: ") 
print(a.department())
q = int(input("Choose:-\n 1. Add employee\n 2. Remove employee\n 3. Total employees\n 4. Salary related information\n  "))
while (True):
    if q == 1:
        print(a.add_emp())
    elif q == 2:
        print(a.remove_emp())
    elif q==3:
        print(a.total_emp())
    elif q==4:
        print(a.salary())
    q = int(input("choose:-\n 1. Add employee\n 2. Remove employee\n 3. Total employees\n 4. Salary related information\n  "))
                
