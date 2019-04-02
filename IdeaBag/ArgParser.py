#Argument Parser program..

import argparse
import sys

def main():

    parser= argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='1st no.')
    parser.add_argument('--y', type=float, default=1.0, help='2st no.')
    parser.add_argument('--oper', type=str, default='add', help='Operator here')
    args= parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.oper is 'add':
        return args.x + args.y
    elif args.oper is 'subs':
        return args.x - args.y
    elif args.oper is 'mul':
        return args.x * args.y
    elif args.oper is 'div':
        return args.x / args.y

if __name__=='__main__':
    main()
