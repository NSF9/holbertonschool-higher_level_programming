#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
     print("{}{}, ".format(i, j) if i + j != 17
           else  "{}{}\n".format(i, j), end="")
