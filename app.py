try:
 print("1-Length\n2-Temperature")
 choice=int(input("Enter your choice:"))#1 - length, 2 - temperatur
 print("")
#1Code for Length
 if choice == 1:
    length= float(input("Enter your length in meters:"))
    print("1-kilometer\n2-feet")

# taking choice from user as ainput
    length_choice = int(input("Enter your choice: "))#1-kilometer, 2-feet
    if length_choice == 1:
        print(f"{length / 1000} kilometer")
    elif length_choice == 2:
        print(f"{length * 3.28084} feet")
    else:
        print
#Code for Temperature
 elif choice == 2:
    temperature = float(input("Enter your temperature in Celsius:"))
    print (f"{(temperature*9/5)+32}Fahrenheit")

 else:
    print("INVALID CHOICE")
except ValueError:
 print("PLEASE TRY AGAIN")

except Exception as e:
    print("Error:")
