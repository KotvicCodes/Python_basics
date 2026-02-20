# input matrixes A and B=I
# totally eliminate A
# apply the same operations to B
# output matrix A^(-1)

#! Build Matrix
A = [] # square matrix A
B = [] # identity matrix B

dimensionOfA = int(input("Input the dimension of the square matrix A: "))

for i in range(dimensionOfA):
    currentRowA = []
    currentRowB = []

    for j in range(dimensionOfA):

        # build A based on user input
        currentElement = float(input(f"Input element #{j+1} in row #{i+1}: "))
        currentRowA.append(currentElement)

        # build B based on kronecker delta
        if i == j:
            currentRowB.append(1)
        else:
            currentRowB.append(0)

    # append rows
    A.append(currentRowA)
    B.append(currentRowB)

#! Gauss Elimination
#* Equalize pivots
def equalizePivots(matrixA, matrixB, i):
    dividedMatrixA = []
    dividedMatrixB = []

    for k, row in enumerate(matrixA):
        dividedRowA = []
        dividedRowB = []
        divisor = row[i]

        if divisor != 0 and not (matrixA[0] == row and i != 0):
            for j, elA in enumerate(row):
                elB = matrixB[k][j]

                if j >= i:
                    dividedRowA.append(elA / divisor)
                    dividedRowB.append(elB / divisor)
                else:
                    dividedRowA.append(elA)
                    dividedRowB.append(elB)
                    print(f"dividedRowA: {dividedRowA}")
                    print(f"dividedRowB: {dividedRowB}")
            dividedMatrixA.append(dividedRowA)
            dividedMatrixB.append(dividedRowB)
        else:
            dividedMatrixA.append(row)
            dividedMatrixB.append(matrixB[k])
    return dividedMatrixA, dividedMatrixB

#* Sum rows
def sumRows(matrixA, matrixB, i):
    summedMatrixA = []
    summedMatrixB = []

    for j, row in enumerate(matrixA):
        if j <= i:
            summedMatrixA.append(row)
            summedMatrixB.append(matrixB[j])
        else:
            summedRowA = []
            summedRowB = []

            for k, elA in enumerate(row):
                elB = matrixB[j][k]

                if row[i] != 0:
                    summedElementA = matrixA[i][k] - elA
                    summedElementB = matrixB[i][k] - elB
                    summedRowA.append(summedElementA)
                    summedRowB.append(summedElementB)
                else:
                    summedRowA.append(elA)
                    summedRowB.append(elB)
            summedMatrixA.append(summedRowA)
            summedMatrixB.append(summedRowB)
    return summedMatrixA, summedMatrixB

#* Sort rows by leading zeros
def sortRows(matrixA, matrixB):
    sortedMatrixA = []
    sortedMatrixB = []
    placeholderMatrixA = []
    placeholderMatrixB = []
    iterationMatrixA = [row[:] for row in matrixA]
    iterationMatrixB = [row[:] for row in matrixB]

    for j in range(dimensionOfA):
        for k, rowA in enumerate(iterationMatrixA):
            rowB = iterationMatrixB[k]

            if rowA[j] != 0:
                sortedMatrixA.append(rowA)
                sortedMatrixB.append(rowB)
            else:
                placeholderMatrixA.append(rowA)
                placeholderMatrixB.append(rowB)

        if j == dimensionOfA - 1:
            sortedMatrixA.extend(placeholderMatrixA)
            sortedMatrixB.extend(placeholderMatrixB)

        iterationMatrixA = [row1[:] for row1 in placeholderMatrixA]
        iterationMatrixB = [row1[:] for row1 in placeholderMatrixB]
        placeholderMatrixA = []
        placeholderMatrixB = []
    return sortedMatrixA, sortedMatrixB

#* Gauss elimination
for i in range(dimensionOfA - 1):
    A, B = equalizePivots(A, B, i)
    A, B = sumRows(A, B, i)
    A, B = sortRows(A, B)

#! Jordan Elimination
def jordanEliminate(matrixA, matrixB):
    for j, rowA in reversed(list(enumerate(matrixA))):
        #* Get 1 on the diagonal
        backsidePivot = matrixA[j][j]
        dividedRowA = []
        dividedRowB = []

        if backsidePivot == 0:
            print("Your matrix is uninvertible")
            exit()
        
        for k, elA in enumerate(matrixA[j]):
            elB = matrixB[j][k]
            dividedRowA.append(elA / backsidePivot)
            dividedRowB.append(elB / backsidePivot)

        matrixA[j] = dividedRowA
        matrixB[j] = dividedRowB

        #* Exit loop, when there is no line above
        if j == 0:
            break

        #* Anullate this column
        for k in range(j):
            currentRowA = matrixA[k]
            currentRowB = matrixB[k]
            lastNonZero = matrixA[k][j]
            summedRowA = []
            summedRowB = []

            for l, elA in enumerate(currentRowA):
                elB = currentRowB[l]
                summedRowA.append(elA - matrixA[j][l] * lastNonZero)
                summedRowB.append(elB - matrixB[j][l] * lastNonZero)
            matrixA[k] = summedRowA
            matrixB[k] = summedRowB
    return matrixA, matrixB

#! Inverse Matrix Finder
def inverseMatrix(A, B):
    print(F"Your inverse matrix of A is A^(-1): {jordanEliminate(A, B)[1]}")
    return None
inverseMatrix(A, B)