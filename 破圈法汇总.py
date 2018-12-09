import copy

#判断矩阵是否含圈
def judge(matrix):
    temporary_matrix=copy.deepcopy(matrix)
    d=[]
    e=[]
    #判断是否含有圈
    #求每个点的度
    for i in range(len(matrix)):
        e.append([])
        for j in range(len(matrix)):
            if matrix[i][j]==0:
                temporary_matrix[i].remove(0)
            else:
                e[i].append(j)
        d.append(len(temporary_matrix[i]))#d为每个点的度数
    c=-1
    m=0
    for i in list(d):
        c+=1
        if i == 1:
            matrix[c][e[c][0]]=0
            matrix[e[c][0]][c]=0
            m=1
    return(m,d)

def judge_circle(d):
    judge=0
    for i in list(d):
        if i == 0:
            judge+=1
    return(judge)#判断数为零表示含圈
    
#含圈则进行破圈法
#寻找最大边，并删除
def max_side(matrix,d):
    max_element=0
    max_i=0
    max_j=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]>=max_element and d[i]>1:
                max_element=matrix[i][j]
                max_i=i
                max_j=j
    matrix[max_i][max_j]=0
    matrix[max_j][max_i]=0
    return(matrix)

matrix=([0,2,2,0,0,0],
        [2,0,2,4,0,0],
        [2,2,0,0,4,0],
        [0,4,0,0,2,2],
        [0,0,4,2,0,2],
        [0,0,0,2,2,0])
a=1
while (a==1):
    (a,d)=judge(matrix)
judge_number=judge_circle(d)
while(judge_number!=len(matrix)):
    matrix=max_side(matrix,d)
    print(matrix)
    b=1
    tem_matrix=copy.deepcopy(matrix)
    while (b==1):
        (b,d)=judge(tem_matrix)
    judge_number=judge_circle(d)
print(matrix)
