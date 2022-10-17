#magic
mat=[[2,7,6],[9,5,1],[4,3,8]]
def is_magic(mat):
    sd1=0
    sd2=0
    for i in range(len(mat)):
        sd1+=mat[i][i]
        sd2+=mat[i][len(mat)-i-1]
    if not(sd1==sd2):
        return False
    for i in range(len(mat)):
        sr=0
        sc=0
        for j in range(len(mat)):
            sr+=mat[i][j]
            sc+=mat[j][i]
    if not(sr==sc==sd1):
        return False
    return True


if(is_magic(mat)):
    print('it is magic matrix')
else:
    print('not magic matrix')
    