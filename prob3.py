#!/usr/bin/env python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrix = "AFKOSWBGLPTXCHMQUYDINRVZEJ"


def encrypt(line):
    l = line.split(" ")
    result = []
    count = int(l[-1]) % 26
    for el in l[:-1]:
        for letter in el:
            result.append(cesar(letter, count))
        result.append(" ")
    return "".join(result)


def cesar(l, c):
    s = chr(((alphabet.index(l) + 1 + c) % 26) + 64)
    return matrix[alphabet.index(s)]


out = open('cesar.out', 'w')
with open('cesar.in', "r") as f:
    lines = f.readlines()
    for line in lines:
        out.write(encrypt(line) + '\n')
    out.close()
    print("Done")
