#spiral
row=int(input('number of rows :'))
col=int(input('number of columns :'))
mat=[]
for i in range(row):
    b=[]
    for j in range(col):
        j=input('the element is ['+str(i)+']['+str(j)+']')
        b.append(j)
    mat.append(b)
print('matrix is :')
for i in range(len(mat)):
    for j in range(len(b)):
        print(mat[i][j], end= ' ')
    print() 
def spiral_mat(mat):
    top=0
    down=row
    left=0
    right=col
    dir=0
    while top<=down and left<=right:
        if dir==0:
            for i in range(left,right):
                print(mat[top][i])
            top+=1
        elif dir==1:
            for i in range(top,down):
                print(mat[i][right-1])
            right-=1
        elif dir==2:
            for i in range(left,right)[::-1]:
                print(mat[down-1][i])
            down-=1
        elif dir==3:
            for i in range(top,down)[::-1]:
                print(mat[i][left])
            left+=1
        dir=(dir+1)%4

 
spiral_mat(mat)   