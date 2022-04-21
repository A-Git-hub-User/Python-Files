# Just a quick script before bed.

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = x + y

print(z)

a = input("Do you want to restart the program? ")
if a == "yes":
    print("Restarting the program...")
    import PythonFile2
elif a == "no":
    print("Ending the program...")
else:
    print("Invalid input. Ending the program...")
