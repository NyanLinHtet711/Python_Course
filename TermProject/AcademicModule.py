#Id: 6411271
#Name: Lynn Thit Nyi Nyi

#DO NOT TOUCH!
import ReadWriteModule
data = ReadWriteModule.readFile("academicrecords")
#DO NOT TOUCH!

def func1():
    temp = []

    temp.append(input("Enter academic year: "))
    temp.append(input("Enter academic term: "))
    temp.append(input("Enter course code: "))
        
    match = False

    for j in range (len(data)): #checking if the course code of the same semester and year exists
        if data[j][0] == temp[0] and data[j][1] == temp[1] and data[j][2] == temp[2]:
            match = True 

    if match == False: #if the course code of the same semester and year doesn't exist
        temp.append(input("Enter section number: ")) #keep asking for other data
        temp.append(input("Enter grade result: ")) #keep asking for other data
        temp.append(input("Enter course credit: ")) #keep asking for other data
        data.append(temp) #append all the data together into the data list
        print (f"{temp[2]} added.")
        
    elif match == True: #if the course code of the same semester and year exists
        print(f"{temp[2]} already exists in {temp[1]}/{temp[0]}.")
    ReadWriteModule.write('academicrecords',data) #overwrite csv file
    print()


def func2():
    match2 = False
    course = input('Enter course code: ')
    for i in range (len(data)): #searching if any row contains the course code
        #print (data[i][2]) #testing
        if (data[i][2]) == course: #searching if any row contains the course code
            print ('Match found!') #testing purposes
            x = i #x = the index for the row that contains the course code
            match2 = True

    if match2 == True: #if course code exists
        data.remove(data[x]) #remove the tow that contains the course using the value of x
        print(f"{course} removed.")
        #test print(data)
    else: #if course code does not exist
        print (f"Error: {course} does not exist!")
        #test print(data)
    ReadWriteModule.write('academicrecords',data) #overwrite csv file
    print()

def func3():
    #so that the original data and list does not get sorted
    temp3 = []
    for each in data:
        temp3.append(each)
    temp3.sort(reverse=True)
    
    seen = set()

    #print out data using the first row
    print(f"Semester {temp3[0][1]}/{temp3[0][0]}") #Latest semester of first year
    print(f"{temp3[0][2]}\t({temp3[0][3]})\t{temp3[0][4]}") #Course code, section and grade
    seen.add(str(temp3[0][0]) + str(temp3[0][1])) #Latest semester of first year added to seen

    #print out data starting from second row
    for i in range(1,len(temp3)):
        temp = str(temp3[i][0]) + str(temp3[i][1])
        if temp not in seen: 
            seen.add(temp) #Add semester of the year to seen...
            print (f"\nSemester {temp[4:5]}/{temp[0:4]}") #... so that a semester of a year will only be printed once
        print(f"{temp3[i][2]}\t({temp3[i][3]})\t{temp3[i][4]}") #Course code, section and grade\
        
    print()

def func4():
    grade = input("Enter grade to look up: ")
    match4 = False
    temp4 = [] #store indices of rows where the grade is A
    for i in range (len(data)):
        if data[i][4] == grade:
            match4 = True
            temp4.append(i)

    if match4 == True:
        for each in temp4:
            print(f"{data[each][2]}\t({data[each][3]})\t{data[each][4]}")
    elif match4 == False:
        print(f"Error: No academic records found for {grade} grade!")
    print()


def func5(): #edit needed to print S last
    temp5 = [['A',0],['A-',0],['B',0],['B-',0],['B+',0],['C',0],['C-',0],['C+',0],['D',0],['F',0],['S',0]]

    for i in range (len(data)): #check grade result in every row
        if data[i][4] == 'A':
            temp5[0][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'A-':
            temp5[1][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'B':
            temp5[2][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'B-':
            temp5[3][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'B+':
            temp5[4][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'C':
            temp5[5][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'C-':
            temp5[6][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'C+':
            temp5[7][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'D':
            temp5[8][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'F':
            temp5[9][1] += 1 #store count of the grade result from if statement
        elif data[i][4] == 'S':
            temp5[10][1] += 1 #store count of the grade result from if statement

    norecord = True #initialise with the condition that there are no academic records
    for k in range (len(temp5)):
        if temp5[k][1] != 0:
            norecord = False #if at least one row has a valid grade result, norecord will become False

    #print grade results and the count ONLY if count > 0
    if norecord == False: 
        for j in range (len(temp5)): 
            if temp5[j][1] > 0:
                print (f"Grade{temp5[j][0]}\t{temp5[j][1]} course(s)")
    elif norecord == True:
        print("Error: No academic records found!") #print error message
    print()


def func6():
    year6 = input('Enter academic year : ') #input year 
    term6 = input('Enter academic term: ') #input term 
    code6 = input('Enter course code: ') #input course
    temp6 = data
    
    match6 = False #initialise with match6 = False
    for i in range (len(data)): #search if there are any records that matches all the criteria
        if temp6[i][2] == code6 and temp6[i][1] == term6 and temp6[i][2] == code6:
            match6 = True #if a record that matches criteria is found, match6 will become True
            x6 = i #X marks the spot
            
    #testing print(data) 
    #testing print(match6)
            
    if match6 == True: #if there is a match
        new_grade = input("Enter grade result: ") #ask for the new grade result to replace the old grade
        data[x6][4] = new_grade #replace using the x6 index
        print(f"Updated grade result {data[x6][1]}/{data[x6][0]} on {data[x6][2]} as {new_grade}")
    elif match6 == False: #if there is no match
        print(f"Error: {code6} not found for {term6}/{year6}!") #error message
    
    print()
    ReadWriteModule.write('academicrecords',data) #overwrite csv file


def func7():
    temp7 = [['S',0],['A',0],['A-',0],['B+',0],['B',0],['B-',0],['C+',0],['C',0],['C-',0],['D',0],['F',0]]

    total_GRWxC = 0
    totalC = 0

    for i in range(len(data)):
        data[i][5] = int(data[i][5])
        if data[i][4] == 'A':
            total_GRWxC += 4*data[i][5]
        elif data[i][4] == 'A-':
            total_GRWxC += 3.75*data[i][5]
        elif data[i][4] == 'B+':
            total_GRWxC += 3.25*data[i][5]
        elif data[i][4] == 'B':
            total_GRWxC += 3*data[i][5]
        elif data[i][4] == 'B-':
            total_GRWxC += 2.75*data[i][5]
        elif data[i][4] == 'C+':
            total_GRWxC += 2.25*data[i][5]
        elif data[i][4] == 'C':
            total_GRWxC += 2*data[i][5]
        elif data[i][4] == 'C-':
            total_GRWxC += 1.75*data[i][5]
        elif data[i][4] == 'D':
            total_GRWxC += 1*data[i][5]
        elif data[i][4] == 'F':
            total_GRWxC += 1*data[i][5]

    for i in range(len(data)):
        if data[i][5] != 0:
            totalC += data[i][5]

    GPA = round(total_GRWxC / totalC,2)
    print (f"G.P.A. is {GPA}")
    print (f"Total Credit is {totalC}")
    print()


def menu():
    print("AcaRec Version 1.0")
    print("PERSONAL ACADEMIC RECORDS")
    print("---- ---- ---- ---- ---- ---- ----")
    print("1. Add new academic record")
    print("2. Remove a specific academic record")
    print("3. Display academic records by semester")
    print("4. Display academic records by grade result")
    print("5. Display the number of courses for each grade results")
    print("6. Update a grade result to a specific academic record")
    print("7. Calculate the overall G.P.A. and total credits")
    print("0. Exit the program")
    print("---- ---- ---- ---- ---- ---- ----")

def userInput():
    while True:
        try:
            uInput = int(input("Enter option (1-7, 0 to exit): "))
        except ValueError:
            print("Sorry I don't understand that\n")
            continue
        else:
            break
    return uInput

def run():
    menu()
    UInput = userInput()
    while UInput != 0:
        if UInput == 1:
            func1()
        if UInput == 2:
            func2()
        if UInput == 3:
            func3()
        if UInput == 4:
            func4()
        if UInput == 5:
            func5()
        if UInput == 6:
            func6()
        if UInput == 7:
            func7()
        menu()
        UInput = userInput()
    print('AcaRec Stopped. See you next time!') 
