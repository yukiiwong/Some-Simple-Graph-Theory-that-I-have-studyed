import copy

def initialize_tree(matrix):#set up a initial matrix 
    inf=1000
    min_tree=copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            min_tree[i][j]=inf
    return (min_tree)


def min_side(matrix):#set the minial side from the matrix
    inf=1000
    min_element=inf
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]<=min_element :
                min_element=matrix[i][j]
                min_i=i
                min_j=j
    return(min_i,min_j,min_element)

def judge(matrix):#get the edge number. and substract branch with iteration.
    inf=1000
    d=[]
    e=[]
    temporary_matrix=copy.deepcopy(matrix)
    for i in range(len(matrix)):
        e.append([])
        for j in range(len(matrix)):
            if matrix[i][j]==inf:
                temporary_matrix[i].remove(inf)
            else:
                e[i].append(j)
        d.append(len(temporary_matrix[i]))#list d is the number of side in every point.
    m=0
    c=-1
    for i in list(d):
        c+=1
        if i == 1:
            tem_matrix[c][e[c][0]]=inf
            tem_matrix[e[c][0]][c]=inf
            m=1#substract the branch .if m==1,keep on substracting.
    return(m,d)

def judge_circle(d):#judge_number can help to judge, if list d is full of zero,there must not be a circle.
    judge_number=0
    for i in list(d):
        if i==0 :
            judge_number+=1
    return(judge_number)

def update_tree(matrix,min_tree,min_i,min_j,min_element,judge_number):
    inf=1000
    if judge_number==len(matrix):
        min_tree[min_i][min_j]=min_element
        min_tree[min_j][min_i]=min_element
        m=0
    else:
        min_tree[min_i][min_j]=inf
        min_tree[min_j][min_i]=inf
    matrix[min_i][min_j]=inf
    matrix[min_j][min_i]=inf
    return (matrix,min_tree)

inf=1000
matrix=([inf,2,2,inf,inf,inf],
        [2,inf,2,4,inf,inf],
        [2,2,inf,inf,4,inf],
        [inf,4,inf,inf,2,2],
        [inf,inf,4,2,inf,2],
        [inf,inf,inf,2,2,inf])

min_tree=initialize_tree(matrix)
for i in range(10):
    (min_i,min_j,min_element)=min_side(matrix)   #寻找最小位置
    min_tree[min_i][min_j]=min_element           #对最小位置试赋值
    min_tree[min_j][min_i]=min_element
    print(matrix,1)
    print(min_tree,1)
    if min_element==inf:
        break
    m=1
    tem_matrix=copy.deepcopy(min_tree)           #对试赋值的矩阵判断是否为圈
    while (m==1):
        (m,d)=judge(tem_matrix)
    judge_number=judge_circle(d)                 #judge_number值为len（matrix）则为树
    (matrix,min_tree)=update_tree(matrix,min_tree,min_i,min_j,min_element,judge_number)#根据判断结果赋值
    k=0
    for i in list(d):
        k=k+i
    print(matrix,2)
    print(min_tree,judge_number,2)

