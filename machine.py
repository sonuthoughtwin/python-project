class Machinev:
    def __init__(self):
        self.a={"Item":"Coke","Price":25}
        self.b={"Item":"Pepsi","Price":35}
        self.c={"Item":"Soda","Price":45}
        self.item=[self.a,self.b,self.c]
        for i in self.item:
            print(i)

        print("Press 1 : Coke\nPress 2 : Pepsi\nPress 3 : Soda")
        self.ch=int(input("Press Key numeric "))

    def choice(self):
        if self.ch==1:
            print("Your Choice is "+str(self.a)+"\nAccepted Coins Only: 1,5,10,25")
            price=1
            amt=0
            while price<=25:
                coins=int(input("Enter coins format"))
                if coins==1 or coins==5 or coins==10 or coins==25:
                    coins_n=int(input("Enter total coins"))
                    amt=amt+(coins*coins_n)                    
                    if amt>=25:
                        print("you buy Coke\nTOTAL DEDUCTION IS "+str(amt)+"\nRemaining amt is "+str(amt-25))
                        print("******Thank you*******")
                        break    
                else:
                    print("Accepted Coins Only: 1,5,10,25")
                price=+1
        if self.ch==2:
            print("Your Choice is "+str(self.b)+"\nAccepted Coins Only: 1,5,10,25")
            price=1
            amt=0
            while price<=35:
                coins=int(input("Enter coins format"))
                if coins==1 or coins==5 or coins==10 or coins==25:
                    coins_n=int(input("Enter total coins"))
                    amt=amt+(coins*coins_n)                    
                    if amt>=35:
                        print("you buy Pepsi\nTOTAL DEDUCTION IS "+str(amt)+"\nRemaining amt is "+str(amt-35))
                        print("******Thank you*******")
                        break    
                else:
                    print("Accepted Coins Only: 1,5,10,25")
                price=+1
        if self.ch==3:
            print("Your Choice is "+str(self.c)+"\nAccepted Coins Only: 1,5,10,25")
            price=1
            amt=0
            while price<=45:
                coins=int(input("Enter coins format"))
                if coins==1 or coins==5 or coins==10 or coins==25:
                    coins_n=int(input("Enter total coins"))
                    amt=amt+(coins*coins_n)                    
                    if amt>=45:
                        print("you buy Soda\nTOTAL DEDUCTION IS "+str(amt)+"\nRemaining amt is "+str(amt-45))
                        print("******Thank you*******")
                        break    
                else:
                    print("Accepted Coins Only: 1,5,10,25")
                price=+1
        else:
            print("Please Press Valid key ")
             
j=True           
while True:
    obj=Machinev()
    obj.choice()
        