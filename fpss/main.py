"""Main entrypoint.

"""

import sys, os
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outdir', type=str, default="out")
    parser.add_argument('--seed', type=int, default=None)
    return parser.parse_args(args)


def main(args):
    outdir = args.outdir
    seed = args.seed
    print("Main function in main.py not implemented!")


#######################
##  Main Entrypoint  ##
#######################

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)

