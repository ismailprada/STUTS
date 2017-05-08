#!/usr/bin/env python3

from collections import Counter

infile = open("newstest2009.de")

word_count = Counter()

for line in infile:
    line = line.split()
    for word in line:
        word_count[word] += 1

for entry in word_count.most_common(100):
    print(entry)

infile.close()
