x=input("Enter a number");
y=input("Enter another number");
def conv(x,y):
    x=int(x);
    y=int(y);
    return x,y;
x,y=conv(x,y);
if(x>y and x!=y):
    print("x is greater");
elif(x == y):
    print("Both are equal");
else:
    print("Y is greater");