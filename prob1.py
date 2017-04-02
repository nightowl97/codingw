#!/usr/bin/env python3

out = open("detect.out", "w")   # Output file
with open("detect.in", "r") as f:
    lines = [i.strip() for i in f.readlines()]
    for line in lines:
        s = 0
        for position, letter in enumerate(line):
            s += (ord(letter) - 64) * (position + 1)    # because ord('A') is 65
        out.write(str(s) + "\n")
    out.close()
    print("done")
