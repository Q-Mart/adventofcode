#!/usr/bin/python
import sys
import os

def k(day):
    return int(day[3:-3])

if __name__ == '__main__':
    year = sys.argv[1]
    files = os.listdir(f'./{year}')
    files.remove('inputs')

    for f in sorted(files, key=k):
        print(f)
