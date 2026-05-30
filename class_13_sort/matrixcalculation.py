def createMatrix(row,col):
    outMatrix = []
    for i in range(row):
        eachRow = [] 
        for j in range(col):
            eachRow.append(int(input(f"Enter an element at row#{i+1} and column#{j+1} :")))
        outMatrix.append(eachRow)
    return outMatrix

def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end = "  ")
        print()


def matrixMultiplication(mat1,mat2):
    result = []
    for each in range(len(mat1)):
        result.append([0 for i in range(len(mat2[0]))])
    for row in range(len(mat1)):
        for column in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                result[row][column] += mat1[row][k]*mat2[k][column]
        
    return result