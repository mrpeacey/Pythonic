with open("details.csv","r") as file:
    detls=file.read().rstrip().split(",");
    
    for i in range(0,2):
        print(f"{detls[i]} is in {detls[i+1]}")
  
     
     