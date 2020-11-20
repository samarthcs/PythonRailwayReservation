def tripint():
##    sizeofrec=20
##    with open("C:\\datafile\\cba.dat",'wb') as file:
        print("Available Destinations")
        print("1 for Delhi to Amritsar")
        print("2 for Delhi to Bengaluru")
        print("3 for Jammu to Lucknow")
        print("4 for Jaipur to Alwar")
        print("5 for Amritsar to Delhi")
        print("6 for Alwar to Bombay")
        print("7 for Bengaluru to Delhi")
        print("8 for Lucknow to Jammu")
        option=int(input("Enter your choice of number for desired trip"))
        if option==1:
            print("Train name:Shatabdi EXPRESS")
            print("cost for this trip is Rs1000")
            print("Duration-21:00-6:00")
            print("Available seats=60/120")
        elif option==2:
            print("Train name:Gatiman EXPRESS")
            print("cost for this trip is Rs1200")
            print("Duration-23:00-9:00")
            print("Available seats=62/120")
        elif option==3:
            print("Train name:Rajdhani EXPRESS")
            print("cost for this trip is Rs1500")
            print("Duration-21:00-11:00")
            print("Available seats=50/120")
        elif option==4:
            print("Train name:Garibrath EXPRESS")
            print("cost for this trip is Rs1250")
            print("Duration-20:00-4:00")
            print("Available seats=64/120")
        elif option==5:
            print("Train name:Shatabdi EXPRESS")
            print("cost for this trip is Rs1101")
            print("Duration-21:30-6:30")
            print("Available seats=80/120")
        elif option==6:
            print("Train name:Shatabdi EXPRESS")
            print("cost for this trip is Rs1000")
            print("Duration-16:00-2:00")
            print("Available seats=36/120")
        elif option==7:
            print("Train name:Gatiman EXPRESS")
            print("cost for this trip is Rs1800")
            print("Duration-21:00-4:30")
            print("Available seats=70/120")
        elif option==8:
            print("Train name:Pooja EXPRESS")
            print("cost for this trip is Rs1600")
            print("Duration-12:00-21:00")
            print("Available seats=10/120")
        with open("C:\\datafile\\cba.dat",'wb') as file:
            file.write(option.encode())
        
##
##        ans='y'
##        while ans=='y' or ans=='Y':
##            name=input("Enter your first name")
##            name1=input("Ënter your last name")
##            age=input("Enter your age")
##            gen=input("Enter your gender")
##            l=len(name)
##            j=len(name1)
##            h=len(gen)
##            name=name+(sizeofrec-1)*' '
##            name1=name1+(sizeofrec-1)*' '
##            gen=gen+(sizeofrec-1)*' '
##            age=age+(sizeofrec-1)*' '
##            file.write(name.encode())
##            file.write(name1.encode())
##            file.write(age.encode())
##            file.write(gen.encode())
##            ans=input("Add more")
