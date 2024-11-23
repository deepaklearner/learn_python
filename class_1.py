class test:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        
    
    def printname(self):
        print(self.fname)
        print(self.lname)

obj1 = test("deepak","raushan")
obj1.printname()