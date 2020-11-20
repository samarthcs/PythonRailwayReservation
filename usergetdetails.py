def userint():
    sizeofrec=20
    with open("C:\\datafile\\abc.dat",'wb') as file:
        ans='y'
        while ans=='y' or ans=='Y':
            name=input("Enter your first name")
            name1=input("Ënter your last name")
            age=input("Enter your age")
            gen=input("Enter your gender")
            l=len(name)
            j=len(name1)
            h=len(gen)
            name=name+(sizeofrec-1)*' '
            name1=name1+(sizeofrec-1)*' '
            gen=gen+(sizeofrec-1)*' '
            age=age+(sizeofrec-1)*' '
            file.write(name.encode())
            file.write(name1.encode())
            file.write(age.encode())
            file.write(gen.encode())
            ans=input("Add more")

    
    ##def userinf():
    ##    import pickle
    ##    k=[]
    ##    with open("C:\\datafile\\cs1.dat", 'wb') as file:
    ##        ans= 'y'
    ##        while ans== 'y':
    ##            name=input("Enter first name")
    ##            ename=input("Enter last name")
    ##            age=int(input("Enter your age"))
    ##            gen=input("enter your sex")
    ##            k.append([name,ename,age,gen])
    ##            ans=input("Add more y/n")
    ##            
    ##            pickle.dump(k,file)
    ##            import pickle
    ##            
    ##            with open("C:\\datafile\\cs1.dat", "rb") as file:
    ##                k=pickle.load(file)
    ##                for e in k:
    ##                    print(e)
                

print("MENU for Railway Reservation")
print("choose from the options given below for your service")
restart = ('Y')
while restart != ('N','NO','n','no'):
    
    print(" PRESS  1 FOR TICKET BOOKINGS")
    print(" PRESS 2 FOR TRAIN DETAILS ")
    print(" PRESS 3 FOR CHECKING PNR STATUS")
    print (" PRESS 4 FOR CANCEL BOOKINGS")

    opt = int(input("\n ENTER YOUR OPTION : "))
    
    if opt==1:
        
        
        people = int(input("\nEnter no. of Ticket you want : "))

        name_l = []
        age_l = []
        sex_l = []
        for p in range(people):
            name = str(input("\nName : "))
            name_l.append(name)
            age  = int(input("\nAge  : "))
            age_l.append(age)
            sex  = str(input("\nMale or Female : "))
            sex_l.append(sex)

        restart = str(input("\nOops! Forget someone : "))
        if restart in ('y','YES','yes','Yes'):
            restart = ('Y')
            break
    
        else:
            x = 0
            print("\nTotal Ticket : ",people)
            for p in range(1,people+1):
                         
                print("Ticket : ",p)
                print("Name : ", name_l[x])
                print("Age  : ", age_l[x])
                print("Sex : ",sex_l[x])
                x += 1
                            
                
                        

                

                
##        
 

    





            
