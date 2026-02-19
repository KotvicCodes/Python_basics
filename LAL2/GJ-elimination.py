# input matrixes A and B=I
# totally eliminate A
# apply the same operations to B
# output matrix A^(-1)

#! Build Matrix
A = []
dimensionOfA = int(input("Input the dimension of the square matrix A: "))

for i in range(dimensionOfA):
    currentRow = []

    for j in range(dimensionOfA):
        currentElement = float(input(f"Input element #{j+1} in row #{i+1}: "))
        currentRow.append(currentElement)

    A.append(currentRow)

#! Gauss Elimination Of A
#* Equalize pivots
def equalizePivots(matrix, i):
    dividedMatrix = []

    for row in matrix:
        dividedRow = []

        if row[i] != 0 and not (matrix[0] == row and i != 0):
            for j, el in enumerate(row):
                if j >= i:
                    dividedRow.append(el / row[i])
                else:
                    dividedRow.append(el)
            dividedMatrix.append(dividedRow)
        else:
            dividedMatrix.append(row)

    print(f"divided: {dividedMatrix}")
    return dividedMatrix

#* Sum rows
def sumRows(matrix, i):
    summedMatrix = []
    for j, row in enumerate(matrix):
        if j <= i:
            summedMatrix.append(row)
            print(f"skipped row: {row}")
        else:
            summedRow = []
            for k, el in enumerate(row):
                if row[i] != 0:
                    summedElement = matrix[i][k] - el
                    print(f"matrix[i][k] {matrix[i][k]}")
                    print(f"el {el}")
                    summedRow.append(summedElement)
                else:
                    summedRow.append(el)
            print(f"summedRow: {summedRow}")
            summedMatrix.append(summedRow)
    return summedMatrix

#* Sort rows by leading zeros
def sortRows(matrix):
    sortedMatrix = []
    placeholderMatrix = []
    iterationMatrix = [row[:] for row in matrix]

    for j in range(dimensionOfA):
        for row in iterationMatrix:
            if row[j] != 0:
                sortedMatrix.append(row)
            else:
                placeholderMatrix.append(row)
        if j == dimensionOfA - 1:
            sortedMatrix.extend(placeholderMatrix)
        iterationMatrix = [row1[:] for row1 in placeholderMatrix]
        placeholderMatrix = []
    return sortedMatrix

#* Gauss elimination
for i in range(dimensionOfA - 1):
    A = equalizePivots(A, i)
    A = sumRows(A, i)
    A = sortRows(A)
    print(f"completed {A}")
