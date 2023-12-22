print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names=name1+""+name2
names=names.lower()
count1=0
count2=0

for t in "true":
  count1+=names.count(t)

for t in "love":
  count2+=names.count(t)

score=int (str(count1)+""+str(count2))

if score<10 or score > 90:
  print ("Your score is "+str(score)+", you go together like coke and mentos.")
elif 40<score<50:
  print ("Your score is "+str(score)+", you are alright together.")
else:
  print ("Your score is "+str(score)+".")