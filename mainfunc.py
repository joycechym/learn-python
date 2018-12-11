def Age():
    age=input("Enter Age : ")
    return age

def Name():
    name=input("Enter Name : ")
    return name


    
def Main():
    nameResult=Name()
    ageResult=Age()
    print("Name is ",nameResult," Age is ",ageResult)

if __name__=="__main__": 
    Main() 
    
    
