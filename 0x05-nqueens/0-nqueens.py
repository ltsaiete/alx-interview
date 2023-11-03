#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem.
"""

import sys

args = sys.argv

if len(args) != 2:
    print('Usage: nqueens N')
    exit(1)

n = args[1]
print(n)
