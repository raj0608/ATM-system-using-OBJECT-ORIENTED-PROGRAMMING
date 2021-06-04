import getpass
class ATM:
    def input(self):
        self.__pin=getpass.getpass(prompt="Enter your pin:")
        self.bal=int(input("Enter your balance:"))
    
    def wd(self):
        e=input("Do you want to withdraw cash yes/no:")
        e.islower()
        if e=="yes":
            self.amt=int(input("Enter the amount you want to withdraw:"))
            if self.bal<self.amt:
                print("Not enough balance!!!")
            elif self.bal>=self.amt:
                print("Transaction successfull")
                self.bal=self.bal-self.amt
                print("New Balance =",self.bal)
        elif e=="no":
            pass
    
    def pc(self):
        z=input("Do you want to change the pin yes/no: ")
        z.islower()
        if z=="yes":
            self.__pin1=getpass.getpass(prompt="Enter your new pin:")
            self.__pin=self.__pin1
        if z=="no":
            pass
    
    def depo(self):
        w=input("Do you want to deposit money yes/no: ")
        w.islower()
        if w=="yes":
            self.dep=int(input("Enter the amount you want to deposit:"))
            self.bal=self.bal+self.dep
            print("New balance is =",self.bal)
        if w=="no":
            pass
        


            
q=ATM()
q.input()
q.wd()
q.pc()
q.depo()
