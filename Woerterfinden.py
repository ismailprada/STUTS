#!/usr/bin/env python3

infile = open("newstest2009.de")

words = []

for line in infile:
    line = line.split()
    for word in line:
        if word[0] == "A" and word[-1] == "s":
            words.append(word)

for word in sorted(set(words)):
    print(word)
