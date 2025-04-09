class library:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.a={}
        self.b={}
        self.c={}

    def book_details(self):
        c = int(input("choose:-\n 1. List of books:\n 2. Books that are currently not in library:\n"))
        if c==1:
            return (self.a)
        elif c==2:
            return(self.c)
        

    def add_book(self):
        v = int(input("choose:-\n 1. Add a new book\n 2. Remove book\n 3. Book's list\n"))
        if v==1:
            book_name = input("Enter book name : ") 
            book_id = int(input("Enter book id: "))
            self.a[book_name]= book_id
            return (self.a)
        elif v==2:
            book_name = input("Enter book name : ") 
            book_id = int(input("Enter book id : "))
            self.a[book_name]= book_id
            self.a.pop(book_name)
            return (self.a)
        elif v==3:
            return (self.a)
        else:
            return ("wrong number....")
            

    def mem_info(self):
        w = int(input("choose:-\n 1. Add a new member\n 2. Remove the member\n 3. Member's list\n"))
        if w==1:
            mem_name = input("Enter member name : ") 
            mem_roll_no = int(input("Enter member roll no: "))
            self.b[mem_roll_no]= mem_name
            return (self.b)
        elif w==2:
            mem_name = input("Enter member name : ") 
            mem_roll_no = int(input("Enter member roll no: "))
            self.b[mem_roll_no]= mem_name
            self.b.pop(mem_roll_no)
            return (self.b)
        elif w==3:
            return (self.b)
        else:
            return ("wrong number....")
            
        

    def transaction(self):
        print("1. Borrow\n 2. Return")
        i = int(input("Enter your choice: "))
        if i == 1:
            bn=input("Enter book name for borrow : ")
            bid=int(input("enter the book id : "))
            rolno=int(input("Enter member roll no : "))
            if bn in self.a:
                if rolno in self.b:
                    self.c[bn]=bid
                    return ("Borrowed ")
        elif i == 2:
            bn=input("Enter book name that has to be returned : ")
            bid = input("Enter book id that has to be returned : ")
            rolno=int(input("Enter member roll no : "))
            if bn in self.a:
                if rolno in self.b:
                    return ("Book has already been returned")
            else:
                self.a[bn] = bid
                return (self.a)
        else:
            return ("Wrong choice......")
mem_name = input("User name: ")
mem_roll_no=int(input("User roll no: " ))
a = library(mem_name, mem_roll_no)
q=int(input("Choose:-\n 1. Book Info\n 2. Member Info\n 3. Transaction\n 4. Book details\n"))
while (True):
    if q==1:
        print(a.add_book())
    elif q==2:
        print(a.mem_info())
    elif q ==3:
        print(a.transaction())
    elif q==4:
        print(a.book_details())
    q=int(input("Choose:-\n 1. Book Info\n 2. Member Info\n 3. Transaction\n 4. Book details\n"))
        
        



    
