
a = int(input("Enter a year:"))

if (a%4==0):
    if(a % 100 == 0):
        if (a % 400 == 0):
            print ("yeeeee leap year")
            
        else:
            print ("Aww not a leap year")
    
    else:
        print ("yeeee leap Year")
        
else:
    print("Aww not a leap year")
    
    
