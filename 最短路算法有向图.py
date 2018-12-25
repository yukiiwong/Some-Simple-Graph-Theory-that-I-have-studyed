
def find_point(adict,alist):
    min_distance = 10000
    k = -1
    for i in alist:
        if adict[i] < min_distance:
            min_distance = adict[i]
            k = i
    return k
inf = 10000
matrix = [[0,1,inf,2,inf,inf],
          [inf,0,3,4,inf,inf],
          [inf,inf,0,5,1,inf],
          [inf,4,inf,0,inf,inf],
          [inf,inf,2,3,0,inf],
          [inf,inf,2,inf,2,0]]
origin = 1   #起点
nodes = [i for i in range(len(matrix))] #未确定的点集数组
visited =[]                              #确定的点集数组
nodes.remove(origin)
visited.append(origin)                  #起点的确定
min_distance = {origin : 0}                         #点的最短距离dict
for i in nodes:
    min_distance[i] = 10000
re_point = [0]*len(matrix)
for i in visited:
    for j in nodes:
        new_distance = min_distance[i] + matrix[i][j]
        if new_distance < min_distance[j]:
            min_distance[j] = new_distance
            re_point[j] = i
    new_point = find_point(min_distance,nodes)
    if new_point == -1:
        print("无法到达点{}".format(nodes))
        nodes.remove(nodes[0])
    else:
        visited.append(new_point)
        nodes.remove(new_point)
        print("%d -> %d" %(re_point[new_point],new_point))
    if nodes == []:
        break
print(min_distance)
