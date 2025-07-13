class office:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.a = {}
        self.b = {}


    def emp_info(self):
        w = int(input("choose 1. add an employee 2. remove 3.total employee"))
        if w==1:
            name = input("enter employees name: ")
            eid = input ("enter employees id: ")
            edep = input("enter employees dep: ")
            self.a[name] = {"id": eid, "dep": edep}
            return self.a
        elif w==2:
            name = input("enter employees name: ")
            eid = input ("enter employees id: ")
            edep = input("enter employees dep: ")
            self.a[name] = {"id": eid, "dep": edep}
            self.a.pop(name)
            return self.a
        elif w==3:
            return self.a
    

    def departments(self): # total number of department or list of employees under each department
        #list of departments
        v = int(input("choose\n 1. Add depatments:\n 2.List of departments"))
        if v==1:
            dep_name = input("enter department name: ")
            dep_id = input ("enter department id: ")
            self.b[dep_name] = dep_id
            return self.b
        elif v==2:
            return self.b


name = input("Admin name: ")
aid = input("Admin id:")
a= office(name, aid)
q = int(input("choose:-\n 1. Employee info\n 2. Department info\n 3. salary calculation"))
while (True):
    print(a.emp_info())
    q = int(input("choose:-\n 1. Employee info\n 2. Department info\n 3. salary calculation"))

        
