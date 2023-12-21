#D3L11.py
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
billAmount=0
if size=='S':
  billAmount=15
elif size=='M':
  billAmount=20
else:
  billAmount=25

if add_pepperoni == 'Y':
  if size=='S':
    billAmount+=2
  else:
    billAmount+=3

if extra_cheese == 'Y':
  billAmount+=1

print ("Your final bill is: $"+str(billAmount)+".")