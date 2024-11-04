#Get the number of rows from the user
n = int(input("Enter the number of rows: "))

#Initialize the current number to 1
current_number = 1

#Looping through each of the row
for i in range(1, n + 1):
    #Print numbers for the current row
    for j in range(1, i + 1):
        print(current_number, end=' ')
        current_number += 1
    #Move to the next line after completing a row
    print()