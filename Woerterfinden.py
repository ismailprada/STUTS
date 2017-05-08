#!/usr/bin/env python3

infile = open("newstest2009.de")

words = set()

for line in infile:
    line = line.split()
    for word in line:
        if word[0] == "A" and word[-1] == "s":
            words.add(word)

for word in sorted(words):
    print(word)

infile.close()
