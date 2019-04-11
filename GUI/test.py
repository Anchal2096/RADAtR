arr =[11,21,31,41,51,61]
m= 2
n= 3
mat= []
index = 0
for i in range(0, m):
    mat.append([])
for i in range (0, m):
    for j in range(0, n):
        mat[i].append(j)
        mat[i][j] = 0
print (mat)
while index < len(arr):
    for i in range (0, m):
        for j in range (0, n):
            print('entry in row ', i+1, 'entry in row ', i+2)

            mat[i][j] = arr[index]
            index = index + 1

print(mat)