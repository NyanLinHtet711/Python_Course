def matrixMultiplication(mat1, mat2):

    result = []

    for i in range(len(mat1)):

        row = []

        for j in range(len(mat2[0])):

            total = 0

            for k in range(len(mat2)):

                total += mat1[i][k] * mat2[k][j]

            row.append(total)

        result.append(row)

    return result


# ---------- Input Matrix 1 ----------

r1 = int(input("Enter rows of Matrix 1: "))
c1 = int(input("Enter columns of Matrix 1: "))

mat1 = []

print("Enter Matrix 1 values:")

for i in range(r1):

    row = []

    for j in range(c1):

        value = int(input(f"mat1[{i}][{j}] = "))
        row.append(value)

    mat1.append(row)


# ---------- Input Matrix 2 ----------

r2 = int(input("Enter rows of Matrix 2: "))
c2 = int(input("Enter columns of Matrix 2: "))

# Matrix multiplication condition
if c1 != r2:
    print("Matrix multiplication not possible")

else:

    mat2 = []

    print("Enter Matrix 2 values:")

    for i in range(r2):

        row = []

        for j in range(c2):

            value = int(input(f"mat2[{i}][{j}] = "))
            row.append(value)

        mat2.append(row)

    # ---------- Multiply ----------

    result = matrixMultiplication(mat1, mat2)

    print("Result Matrix:")

    for row in result:
        print(row)