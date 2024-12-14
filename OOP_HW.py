from datetime import datetime

class Passport:

    def __init__(self,fname,lname,birthday,gender,abiding_place):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.gender = gender
       

        self.abiding_place = abiding_place

    def __del__(self):
        print("--- Passport destructor ---")

    def show(self):
        print(
            f"Passport info:\nFirst name: {self.fname}\nLast name: {self.lname}\nBirthday:{self.birthday.strftime('%d/%m/%Y')}"
        )


pass1 = Passport("Roman","Matviychuk",datetime(2007,1, 12),"Man","Ukraine")
pass1.show()

class ForeignPassport(Passport):
    def __init__(self,fname,lname,birthday,gender,abiding_place):
        
        super().__init__(fname,lname,birthday,gender,abiding_place)
        self.visas = []

    def add_visa(self, visa):
        self.visas.append(visa)
    
    # def remove_visa(self, fname):
    #     for fname in self.visas:
    #         if visa.fname == fnamme



    def __str__(self):
        return f"He has visa #{self.visas}"
    
foreign = ForeignPassport("Mykola","Shevchenko",datetime(2000,1,1),"Man","Poland")
print(foreign)