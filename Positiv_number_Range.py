
Number_List = []

number = int(input("Enter the number of elements in List :"))
for i in range(1,number+1):
    value = int(input("Enter the Value of %d Element :"%i))
    Number_List.append(value)
print("The positive number in the list are :")
for j in range(number):
    if(Number_List[j] >= 0):
        print(Number_List[j],end=" ")



