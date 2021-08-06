import random
import constants_1

def inst_two(M,n):
    x,y = random.randint(0,n-1),random.randint(0,n-1)
    while (M[x][y] != 0):
        x,y = random.randint(0,n-1),random.randint(0,n-1)
    M[x][y] = 2
    return M

def reset(n):
    mat = [[0] for i in range(n)]
    mat = inst_two(inst_two(mat,n),n)
    return mat  

def rev(M):
    m,M_r = len(M),[]
    for i in range(m):
        l = M[i].reverse()
        M_r.append(l)
    return M_r

def transpose(M):
    M_t = []
    for i in range(len(M[0])):
        l = []
        for j in range(len(M)):
            l.append(M[j][i])
        M_t.append(l)
    return M_t

def merge(M,flag):
    for i in range(constants_1.grid_coord[1] - 1):
        for j in range(constants_1.grid_coord[1] - 1):
            if (M[i][j] == M[i][j+1] and M[i][j] != 0):
                M[i][j] += M[i][j+1]
                M[i][j+1] = 0
                flag = True
    return M,flag 

def adjust(M):
    mat = [[0 for j in range(constants_1.grid_coord[1])]for i in range(constants_1.grid_coord[1])]
    flag = False
    for i in range(constants_1.grid_coord[1]):
        c = 0
        for j in range(constants_1.grid_coord[1]):
            if (M[i][j] != 0):
                mat[i][c] = M[i][j]
                if (j != c):
                    flag = True
                c += 1
    return mat,flag

def move(M,dir):
    if (dir == "up"):
        M = transpose(M)
        M,flag = adjust(M)
        M,flag = merge(M,flag)
        M = adjust(M)[0]
        M = transpose(M)
        return M,flag

    elif (dir == "left"):
        M,flag = adjust(M)
        M,flag = merge(M,flag)
        M = adjust(M)[0]
        return M,flag
    
    elif (dir == "down"):
        M = transpose(M)
        M = rev(M)
        M,flag = adjust(M)
        M,flag = merge(M,flag)
        M = adjust(M)[0]
        M = rev(M)
        M = transpose(M)
        return M,flag
    
    else:
        M = rev(M)
        M,flag = adjust(M)
        M,flag = merge(M,flag)
        M = adjust(M)[0]
        M = rev(M)
        return M,flag


def state(M):
    m,n = len(M),len(M[0])

    for i in range(m):
        for j in range(n):
            if (M[i][j] == 2048):
                return 1
    for i in range(m):
        for j in range(n):
            if (M[i][j] == 0):
                return 2
    for i in range(m-1):
        for j in range(n-1):
            if (M[i][j]==M[i+1][j] or M[i][j]==M[i][j+1]):
                return 2
    for i in range(m-1):
        if (M[m-1][i] == M[m-1][i+1]):
            return 2
    for i in range(m-1):
        if (M[i][m-1] == M[i+1][m-1]):
            return 2
    return 0

