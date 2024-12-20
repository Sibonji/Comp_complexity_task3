import math as mt
import time
import json
import sys

filename = 'create_data/data.json'
test = 0
arg_num = len(sys.argv)
if arg_num == 2:
    if sys.argv[1] == "-test":
        test = 1
        filename = 'create_data/test.json'
    else:
        print("You can use -test to check if programm is working correctly")


def distance(x1, y1, x2, y2):
    return mt.sqrt((x2-x1)**2 + (y2-y1)**2)

INF = 2 ** 31-1

v1 = []
with open(filename, 'r') as file:
    data = json.load(file)

points = json.loads(data)

input_matrix = []
for i, vi in points.items(): 
    m1 = []
    for j, vj in points.items():
        if i==j:
             m1.append(INF)
        else:
            m1.append(int(distance(vi[0], vi[1], vj[0], vj[1])))
            v1.append([i,j,int(distance(vi[0], vi[1], vj[0], vj[1]))])
    input_matrix.append(m1.copy()) 
    
#-----------------------------------------------------------------
def tsp(input_matrix):    
    n = len(input_matrix)
    s = (1 << (n - 1)) - 1
    path = [0] * s
    local_sum = [0] * s     
    
    for i in range(s): 
        path[i] = [0] * (n-1)
        local_sum[i] = [-1] * (n-1)  
    m = [n - 1, input_matrix.copy(), path, local_sum]
          
    sum_path = INF
    for i in range(m[0]):       
        index = 1 << i
        if s & index != 0: 
            sum_temp = tsp_next(m, s ^ index, i) + m[1][i + 1][0]
            if sum_temp < sum_path:              
                sum_path = sum_temp
                m[2][0][0] = i + 1
    m[3][0][0] = sum_path
    
    res = []
    init_point = int(path[0][0])
    res.append(init_point)
    s = ((1 << m[0]) - 1) ^ (1 << init_point - 1)
    for i in range(1, m[0]):
        init_point = int(path[s][init_point - 1])
        res.append(init_point)
        s = s ^ (1 << init_point - 1)
    res.append(0)
    return [sum_path, res]

def tsp_next(m, s, init_point):
    if m[3][s][init_point] != -1: 
        return m[3][s][init_point] 
    if s == 0:
        return m[1][0][init_point + 1]
    sum_path = INF
    for i in range(m[0]):        
        index = 1 << i
        if s & index != 0:   
            sum_temp = tsp_next(m, s ^ index, i) + m[1][i + 1][init_point + 1]
            if sum_temp < sum_path:
                sum_path = sum_temp
                m[2][s][init_point] = i + 1
    m[3][s][init_point] = sum_path
    return sum_path

start = time.time()
res = tsp(input_matrix)
end = time.time()
print('min:', res[0])
print(res[1])
print('time taken in ms:', (end - start) * 1000)