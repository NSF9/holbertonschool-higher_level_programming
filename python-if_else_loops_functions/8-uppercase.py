#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i) - 32)
              if ord(i) in range(ord('a'), ord('z') + 1)
              else "{}".format(i), end="")
    print()
