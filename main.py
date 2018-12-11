'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
intvar=2
floatvar=1.4
strvar="Hello World"
charvar='c'
print("intvar is ",intvar)
print("floatvar is ",floatvar)
print("strvar is ",strvar)
print("charvar is ",charvar)

#this is a single line comment
""" multiple line comment
therefore write whatever you want therefore 
and no offense """

#Data structures in python are list, tuples, set and dictionary
#create a list
mylist=[]
mylist.append(2)
mylist.append(1.77)
mylist.append("Joyce's String in the list")
mylist.append('k')
print(mylist)

#Get info from input
name=input("Please enter your name: ")
print("Hello ",name)

num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
result=num1*num2
print("Multiple result of ",num1,"*",num2," is ",num1*num2)

#python selection statement
if(num1>10):
    print("Number is more than 10")
elif(num1<10 and num1>1):
    print("Number is between 1 and 10")
else:
    print("Number is less than or equal 1")
    
def hellofunc():
    print("hellofunc here")
    msg=input("enter a hello message : ")
    print(msg)

#Now call the function
hellofunc()

