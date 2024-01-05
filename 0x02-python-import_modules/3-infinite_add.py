#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    num = 0
    if n <= 1:
        print(0)
    else:
        for i in range(1, n):
            num = int(sys.argv[i]) + num
        print(num)


if __name__ == "__main__":
    main()
