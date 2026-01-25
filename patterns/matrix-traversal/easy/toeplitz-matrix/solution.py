def isToeplitzMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if diagonal position is in bounds
            if i+1 in range(len(matrix)) and j+1 in range(len(matrix[0])):
                if matrix[i+1][j+1] != matrix[i][j]:
                    return False

    return True
