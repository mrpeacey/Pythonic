#what if we have to one key associated to multiple values just like the database than
#we can combine list and dictionary
students = [
    {"name":"ram","age":"24"},
    {"name":"hari","age":"26"},
    {"name":"sita","age":"25"},
];
for i in students:                       #more simple
    print(i["name"]);# i as  a dictionary
    print(i);#i as a list