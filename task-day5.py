#1) create a function getting two integer inputs from user.& print the following:
#a) Addition of two number is + value

def addition(a,b):
add=a+b
print("addition of two numbers:",a+b)
addition(90,80)
#output= addition of two numbers: 170

#b) Subraction of two numbers is + value

def subraction(a,b):
sub=a-b
print("subraction of two numbers:",a-b)
subraction(90,80)
#output= subraction of two numbers: 10

#c) Division of two numbers is + value

 def division(a,b):
 div=a/b
 print("division of two numbers:",a/b)
 division(90,80)

 #output=division of two numbers: 1.125

#d) Multiplication of two numbers is + value

def multiplication(a,b):
mul=a*b
print("multipication of two numbers:",a*b)
multiplication(90,80)

#output= multipication of two numbers: 7200

#2) create a function covid() & it should accept patient name,and body temperature,by default the body temperature should be 98 degree:

def covid(patient_name):
print("Name of the patient:"+patient_name+"")
covid('zebu')

#output= Name of the patient:zebu

def covid(body_temperature):
print("Body temperature of the patient:"+body_temperature+"")
covid('98 degree')

#output= Body temperature of the patient:98 degree
