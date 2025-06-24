num=int(input("Enter a number:"));
def is_even(num):
    if(num%2==0):
        return True;

    else :
        return False;
def check_evnod(num):
    return True if num%2==0 else False;

check=is_even(num);
if(check):
    print("Is even");
else:
    print("Is odd");
check1=check_evnod(num);
if(check1):
    print('evennn');
else:
    print("Odd");