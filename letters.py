#-*- coding: utf8 -*-
import sys

def counter(text):
    letters = {}
    for symbol in text:
        print symbol
        if symbol in letters:
            letters[symbol] += 1
        else:
            letters[symbol] = 1
    return letters


def main():
    for text in sys.argv[1:]:
        for k, v in counter(text).items():
            print k, "=", v

if __name__=="__main__":
    main()

