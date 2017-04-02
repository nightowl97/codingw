#!/usr/bin/env python3

dic = {"a": "2", "b": "22", "c": "222", "d": "3", "e": "33", "f": "333", "g": "4", "h": "44", "i": "444",
       "j": "5", "k": "55", "l": "555", "m": "6", "n": "66", "o": "666", "p": "7", "q": "77", "r": "777", "s": "7777",
       "t": "8", "u": "88", "v": "888", "w": "9", "x": "99", "y": "999", "z": "9999", " ": "0"}


def parse(l):
    result = []
    count = 0
    for letter in l:
        result.append(dic.get(letter))
        count += len(dic.get(letter))
    return ",".join(result) + "\t" + str(count)

out = open("clavier.out", "w")
with open("clavier.in", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
        out.write(parse(line) + "\n")
    out.close()
    print("Done")
