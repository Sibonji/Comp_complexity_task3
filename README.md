# Comp_complexity_task3
Repo for assignment 3: study the approximation of NP-hard problem solutions in Computational complexity course

## Part1 (brute force algorithm)
I will cover Traveling Salesman Problem (TSP) (symmetrical to be fair). Solution will be written on Python, for the part1 it is brute force alghorithm - checking all possible permutations of cities to find the shortest route.

To test code (file create_data/test.json - do not change it) you can run:
```
python3 part1.py -test
```

To run code with data in create_data/data.json file you need to type:
```
python3 part1.py
```

To regenerate data switch to create_data folder and run:
```
python3 write_data.py
```

Runtime complexity can be estimated as O((n-1)!/2). In every city traveller has to choose between all other cities that he had not visited (because there is no difference if he goes from city 2 to 3 or 3 to 2, we need to divide number of all possible solutions by two). 

For 11 cities code execution took 4260 ms, here is the output:
```
time taken in ms: 4260.816812515259
```

And for the 12 cities, according to theory, it will take 12-1 = 11 times more:
```
time taken in ms: 49144.36960220337
```

4261 * 11 = 46871. So theory pretty mich come up with execution results.

## Part2 (dynamic programming algorithm)

The essence of the method is that a city is selected, and then all possible routes are built for all other cities in conjunction with it, and the shortest one is selected. The algorithm is recursively applied to all remaining cities minus the one selected at the previous stage, and so on until only two cities remain unselected. For a symmetrical problem (I will write code for this one), some of the routes will be repeated, and if the result is saved separately, it only needs to be calculated once.

In the process of work we need to store all possible combinations of constructed routes, as well as the length of the minimum route at the moment.

To do this, we will need two arrays of additional memory with (n-1)*$2^{(n-1)}$ elements. The first one is needed to store the local sum at the step, and the second array will contain the path to the vertex, along which we need to move in order to choose the shortest route. If in the end only the value of the optimal solution is needed, then the second array can be completely abandoned, reducing the operating time and the amount of memory used.

For the runtime and computational complexity, we will have O((n-1)*$2^{(n-1)}$).

To run code with data in create_data/data.json file you need to type:
```
python3 part1.py
```

For 11 cities code execution took 10 ms, here is the output:
```
time taken in ms: 9.94253158569336
```

And for the 12 cities, according to theory, it will take 1.1*2 = 2.2 times more:
```
time taken in ms: 24.45054054260254
```

10*2.2 = 22. So theory pretty mich come up with execution results.

Also there is some results for the same data (11 cities). Brute force:
```
min: 3460
[7, 2, 6, 5, 3, 8, 0, 9, 4, 1, 10]
time taken in ms: 4768.43786239624
```

Dynamic programming:
```
min: 3460
[8, 3, 5, 6, 2, 7, 10, 1, 4, 9, 0]
time taken in ms: 9.94253158569336
```

If we look closely, route array and route length are the same.
