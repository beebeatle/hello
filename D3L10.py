# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
isLeap=False


if year%4==0:
  if year%100==0:
    if year%400==0:
      isLeap=True
    else:
      isLeap=False
  else:
    isLeap=True
else:
  isLeap=False

if isLeap is True:  
  print ("Leap year")
else:
  print ("Not leap year")