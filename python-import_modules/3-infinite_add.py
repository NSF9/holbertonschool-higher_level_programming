#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    Result = 0

    for i in range(argc):
        Result += int(argv[i])
        print(Result)
