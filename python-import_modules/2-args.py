#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    if argc == 1:
        print(f"1 argument:\n1:{argc[0]}")
    if argc > 1:
        print(f"{argc} argument:")
        for i, arg in enumerate(argv):
            print(f"{i + 1}: {arg}")
