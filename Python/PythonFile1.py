# This program will allow the user to do mutiple calculations.
# Made by @XeeZisCool on Replit.

# Imports
import math

print("[1] 2 Number Problem")
print("[2] 3 Number Problem")
print("[3] Find a power-of")
print("[4] Find Square Root\n")

try:
  mathtype = (int(input("What type of math are you doing? ")))
except:
  quit("ERROR: Please enter a number")

# How to scare a non-python coder 101 (Or experienced coders)
# Spam if, and elif (elseif).
try:
  
  # 2 Number Problem
  if mathtype == 1:
    try:
      
      x = (float(input("Enter your first number: ")))
      op = (int(input("What are you doing? [1 (+), 2 (-), (3) x, (4) /]: ")))
      y = (float(input("Enter your second number: ")))
      ans = 0

      # Add
      if op == 1:
        ans = (x+y)
        print(ans)
        
      # Sub
      if op == 2:
        ans = (x-y)
        print(ans)

      # Mul  
      if op == 3:
        ans = (x*y)
        print(ans)

      # Div
      if op == 4:
        ans = (x/y)
        print(ans)
        
    except:
      quit("ERROR: Please enter a number")

        
  # 3 Number Problem
  elif mathtype == 2:
   try:
      x = (float(input("Enter your first number: ")))
      op = (int(input("What are you doing? [1 (+), 2 (-), (3) x, (4) /]: ")))
      y = (float(input("Enter your second number: ")))
      op2 = (int(input("What are you doing? [1 (+), 2 (-), (3) x, (4) /]: ")))
      z = (float(input("Enter your third number: ")))
      temp1 = 0
      ans = 0

      # Add
      if op == 1:
        temp1 = (x+y)
        
        #Add Pt. 2
        if op2 == 1:
          ans = (temp1+z)
          print(ans)

        # Sub Pt. 2
        if op2 == 2:
          ans = (temp1-z)
          print(ans)

        # Mul Pt. 2
        if op2 == 3:
          ans = (temp1*z)
          print(ans)

        # Div Pt. 2
        if op2 == 4:
          ans = (temp1/z)
          print(ans)
          
      # Sub
      if op == 2:
        temp1 = (x-y)

        #Add Pt. 2
        if op2 == 1:
          ans = (temp1+z)
          print(ans)

        # Sub Pt. 2
        if op2 == 2:
          ans = (temp1-z)
          print(ans)

        # Mul Pt. 2
        if op2 == 3:
          ans = (temp1*z)
          print(ans)

        # Div Pt. 2
        if op2 == 4:
          ans = (temp1/z)
          print(ans)

      # Mul  
      if op == 3:
        ans = (x*y)
        print(ans)
        
        #Add Pt. 2
        if op2 == 1:
          ans = (temp1+z)
          print(ans)

        # Sub Pt. 2
        if op2 == 2:
          ans = (temp1-z)
          print(ans)

        # Mul Pt. 2
        if op2 == 3:
          ans = (temp1*z)
          print(ans)

        # Div Pt. 2
        if op2 == 4:
          ans = (temp1/z)
          print(ans)

      # Div
      if op == 4:
        ans = (x/y)
        print(ans)
        
        #Add Pt. 2
        if op2 == 1:
          ans = (temp1+z)
          print(ans)

        # Sub Pt. 2
        if op2 == 2:
          ans = (temp1-z)
          print(ans)

        # Mul Pt. 2
        if op2 == 3:
          ans = (temp1*z)
          print(ans)

        # Div Pt. 2
        if op2 == 4:
          ans = (temp1/z)
          print(ans)
        
   except:
      quit("ERROR: Please enter a number")


  #  Power-Of   
  elif mathtype == 3:
    x = (int(input("What is the number you wanna raise the power of?  ")))
    y = (int(input("What is the power?  ")))
    temp1 = 0
    temp1 = math.pow(x, y)
    print(temp1)

  # Sqrt
  elif mathtype == 4:
    x = (int(input("What is the number you wanna find the square-root of?  ")))
    temp1 = 0
    temp1 = math.sqrt(x)
    print(temp1)
    
except:
  quit("ERROR: Advancement Unlocked: How did we get here?")
  
# Not Valid Number
# If this is a dumb way of doing this then well... Screw it.
# TODO: Figure out out to make this message not print after doing math.
# Fix Later!
# if mathtype <= 5:
#     quit("Please Enter a Valid Number [1-4]")

# I don't feel motivated to do this. But still. I want this done.
