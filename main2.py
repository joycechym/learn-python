

def loop():
    rangenum=int(input("Enter a number : "))
    for step in range(rangenum):
        print(step)
        
def Main():
    print("Hello from Main")
    loop()

if __name__=="__main__": 
    Main() 

print(None==0)

x=None
y=None
print(x==y)

print(True or False)
print(False and True)
print(not True)

a=[1,2,3]
print("print before delete ",a)
del a[1]
print("print after delete ",a)
a.append(4)
print("print after append ",a)

#assert 5<3,"5 is not less than 3"

if 's' in 'geeksforgeeks':
    print("s is in geeksforgeeks")
else:
    print("s is not in geeksforgeeks")

for i in 'geeksforgeeks':
    print(i,end="**")  #insert ** in between each character

print('\r')
r=4
print(r is 3)



