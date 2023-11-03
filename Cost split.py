#this asks for the total bill and the ammount of tip you are giving 
while True:

    TA = input("how much do you what to split: ")

    SA = input("split among how many people? ")

#this dose all of the calculation that is needed to find the bill after tip
    cal = float(TA) / float(SA)

#this prints the out of how much the new bill will be 
    print("you'r per head is:",cal)
    
#this ask the user if they would like to use this again
    Again = input("do you what to use it again? ")
    if Again == "yes":
        pass
    elif Again == "no":
        break
    else: print("not a valid answer.")