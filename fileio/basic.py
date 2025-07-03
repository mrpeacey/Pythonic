name=input("Whats you name?");
file=open("name.txt","a");
file.write(f"{name} ");

file.close();
with open("hello.txt","r") as file:
    all=file.read();
    print(all);
with open("name.txt","r") as file:

    print(sorted(file));