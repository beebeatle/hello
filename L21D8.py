# Write your code below this line 👇
def prime_checker(number):
  message="It's a prime number."
  for n in range (2,number):
    if number%n==0:
      message="It's not a prime number."
      break
      
  print (message)




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)