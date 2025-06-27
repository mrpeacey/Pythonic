
try:
    x=int(input("enter any number:"));#the input should be taken inside the try if it is taken outside
                                      #it will just simply display ValueError
    
except :
    print("Error occured");
#print("THE value is",x);#nameerror-> cause when we input string it doesnot get assigend to the x thus x is not actually a variable holding a value
else :
    print("The value is ",x);
    #except ErrorType:
    #if error is not known this can be used this simply is try and catch
    #if error occurs it goes except(maybebadpractice)
    #valueerror-> occurs if data of different datatype is given 