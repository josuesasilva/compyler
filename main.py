#!/usr/bin/env python3

import sys
from scanner.scanner import Scanner
from scanner.token import TokenEnum
from parser.ll_1 import LL1

def main():
    print("\nStarting compiler...\n\n")
    
    file = None
    
    try:
        if len(sys.argv) > 1:
            file = open(sys.argv[1], 'r')    
        else:
            file = open('tests/program.po', 'r')
    except IOError:
        print("Error: File does not appear to exist.")
        return

    scanner = Scanner(file)
    scanner.scan()
    tokens = scanner.tokens_list
    print(tokens)
    print("\n\n")
    parser = LL1(tokens)
    parser.parse()

if __name__ == "__main__":
    main()
