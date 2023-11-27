#single level inheritance
#use the properties and methods of your base class or parent class

class Father:
    bank_bal=5000000000000
    def one_bhk(self):
        print("Use it son")


class Son(Father):
    pass # I will write the code in future !! SKIPPED

s=Son()
s.one_bhk()
print(s.bank_bal)