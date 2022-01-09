numList = [] 
j = 0 
number = int(input("Please enter the Total Number of List Elements: ")) 
for i in range(1, number + 1): 
value = int(input("Please enter the Value of %d Element : " %i)) 
numList.append(value)
print("\nPositive Numbers in this List are : ") 
while(j < number): 
if(numList[j] >= 0): 
  print(numList[j], end = ' ') 
j = j + 1