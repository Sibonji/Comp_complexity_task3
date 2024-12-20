import math as mt
from bitarray import bitarray
import json
import time
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
    return mt.sqrt((x2 - x1) ** 2 + (y2 - y1)**2)

INF = 2 ** 31 - 1


v1 = []
with open(filename, 'r') as file:
    data = json.load(file)

points = json.loads(data)

n = len(points)

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
    
def calc_next(m, s, n, src):
    min = INF
    for i, val in enumerate(s.tolist()):
        if val == 0:           
            s0 = s.copy()
            s0[i] = 1
            if n > 2:
                sum = m[src][i]
                r = calc_next(m, s0, n - 1, i)
                sum = sum + r[0]
                temp = r[1]
            else:   
                for j, val_j in enumerate(s0.tolist()):
                    if val_j == 0:
                        break              
                temp = [j]
                sum = m[src][i] + m[i][j] + m[j][len(m) - 1]
            temp.append(i)
            if sum < min:
                min = sum
                temp2 = temp.copy()
    return [min, temp2]            

start = time.time()
s = bitarray(n - 1)
s.setall(0)
res = calc_next(input_matrix, s, n - 1, n - 1);
res[1].append(n - 1)  
end = time.time()

print('min:', res[0])
print(res[1])
print('time taken in ms:', (end - start) * 1000)

if test == 1:
    correct_route = [3, 0, 2, 1, 4]
    print("min is correct:", res[0] == 277)
    print("route is correct:", res[1] == correct_route)