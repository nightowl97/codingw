#!/usr/bin/env python3

out = open("premiers.out", "w")
with open("premiers.in") as f:
    numbers = [int(i.strip()) for i in f.readlines()]   # List of numbers from input
    for i in numbers:
        current = i
        div = 2
        factors = []
        while current > 1:
            if current % div == 0:
                factors.append(str(div))
                current /= div
            else:
                div += 1
        out.write(str(i) + "=" + "*".join(factors) + "\n")
    out.close()
