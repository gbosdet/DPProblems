import numpy as np

translate = {"a":0, "b":1, "c":3}
arr = [[1, 1, 0], [2, 1, 0], [0, 2, 2]]

string = "abcabc"


def possibilities(string):
    n = len(string)
    arr = np.zeros((n, n, 3), dtype=np.int)
    for i in range(n):
        arr[i, i, translate[string[i:i+1]]] = 1
    for s in range(1, n):
        



print(possibilities(string))