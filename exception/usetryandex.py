def check():
 while True:
    try:
        x=int(input("Enter number"));
    except:
        
        print("Invalid Input");
    else:
        return x;

def main():
    print(check());
main();#before we use function it should be define