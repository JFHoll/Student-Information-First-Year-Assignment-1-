#Jennifer Holland Assignment 1
userInput = str(input("Enter the forename, surname and ID number separated by spaces. If you wish to end, please enter 0."))
#declare empty lists
forenames = []
surnames = []
idNumbers = []

#split userInput into forename surname and id Number and append the information to the appropriate list.
#Continue to ask for information until user enters "0"
while userInput:
    if "0" in userInput:
        break
    userList = userInput.split()
    forenames.append(userList[0])
    surnames.append(userList[1])
    idNumbers.append(userList[2])
    userInput = input("Enter the forename, surname and ID number separated by spaces. If you wish to end, please enter 0.")

#declare studentInfo as a list of lists or 2D Array
studentInfo = [[forenames], [surnames], [idNumbers]]
search = input("Please enter the student ID number or enter 0 to end.")

while search:
 #Continue to search until the user enters 0.
    if search == "0":
        break
    #Search each individual element
    for row in studentInfo:
        for col in row:
 #If the value of search is in the array, find the index and then print the
 #forename, surname, and idNumber with that index.
            if search in col:
                index = idNumbers.index(search)
                print(forenames[index], surnames[index], idNumbers[index])
                search = input("Please enter the student ID number.")