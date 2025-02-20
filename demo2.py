class data:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class college(data):
    def __init__(self,sname,sage,cname,roll):
        self.cname=cname
        self.roll=roll
        super().__init__(sname,sage)
    def printdata(self):
        print("my name is ",self.name," and age is ",self.age,"college : ",self.cname,"roll no.",self.roll)

o1=college("keshav rana",20,"siet",129)
o1.printdata()

