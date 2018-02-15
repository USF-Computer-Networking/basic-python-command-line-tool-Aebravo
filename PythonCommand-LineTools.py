# !/usr/bin/python
from argparse import ArgumentParser
import argparse
from functools import reduce

def main():
    ap = ArgumentParser()
    ap.add_argument('-s', '--sum', action='store_const', const = sum, default = max, dest = "sum", help="Summation of integers(returns max if sum argument is not called", required = False)
    ap.add_argument('--string_list', help = "Create a list of Strings", dest = "stringList", nargs = '+')
    ap.add_argument('--int_list', help = "Create a list of ints (Can use for summation function)", type = int, dest = 'intList', nargs = '+')
    ap.add_argument('-u', '--uppercase', type = lambda s : s.upper(), help="capitalize strings in result", dest = "u")
    ap.add_argument('-l', '--lowercase', type = lambda s : s.lower(), help="lowercase strings in result", dest = "l")
    ap.add_argument('-f', '--file', type=argparse.FileType('r'), dest = "file")
    ap.add_argument('--square', type = int, dest = "square", help = "Enter an integer to square")
    def multiply(n):
        return reduce(lambda x, y: x*y, n)
    ap.add_argument('-m', '--multiply', action='store_const', const=multiply, default=max, dest="multiply", help="Multiplication of integers(returns max if sum argument is not called", required = False)



    args = ap.parse_args()
    if args.u:
        print(args.u)
    if args.l:
        print(args.l)
    if args.intList:
        print(args.intList)
    if args.stringList:
        print(args.stringList)
    if args.file:
        print(args.file.readline())
    if (args.square):
        print(args.square**2)
    if (args.intList):
        print(args.multiply(args.intList))
    if (args.intList):
        print(args.sum(args.intList))


if __name__ == "__main__":
    main()

