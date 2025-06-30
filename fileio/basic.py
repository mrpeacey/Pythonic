name=input("Whats you name?");
file=open("new.txt","a");
file.write(f"{name}\n");

file.close();
with open("hello.txt","r") as file:
    all=file.read();
    print(all);
