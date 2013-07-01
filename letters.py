#-*- coding: utf-8 -*-
import sys

def counter(text):
    letters = {}
    for symbol in text:
        if symbol.isalpha():
            if symbol in letters:
                letters[symbol] += 1
            else:
                letters[symbol] = 1
    return letters


def main():
    text = ' '.join(s.decode("utf-8") for s in sys.argv[1:])
    presorted = list(counter(text).items())
    presorted.sort(key = lambda item: item[1], reverse=True)
    for k, v in presorted:
        print k, "=", v

if __name__=="__main__":
    main()

