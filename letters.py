#-*- coding: utf8 -*-
import sys 

def counter(letters,text):
    for symbol in text:
        if symbol in letters:
            letters[symbol] += 1
        else:
            letters[symbol] = 1
    return letters


def main():
    letters = {}
    for text in sys.argv[1:]:
        presorted = list(counter(letters,text).items())

    presorted.sort(key = lambda item: item[1])
    presorted.reverse()
    for k, v in presorted:
        print k, "=", v

if __name__=="__main__":
    main()

