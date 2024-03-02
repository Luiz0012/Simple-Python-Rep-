#Simple Program That accepts user input and give out a message using the inputs

name = input("Please enter your name : ")
age = int(input("Enter your current age : "))
location = input("Enter your current location.  ")

print(" Hello " , name , ", its good to know you. " )
print(" You are ", age , "years old and living in", location , "." )
print(" To appreciate you responding to my request, I'll get you a gift when you turn ", age+1 , "years old. I'll send it to", location ,"." )
