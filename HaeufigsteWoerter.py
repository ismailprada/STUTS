#!/usr/bin/env python3

import string

infile = open("newstest2009.de")

word_counting_dict = {}

for line in infile:
    line = line.split()
    for word in line:
        if word in word_counting_dict:
            word_counting_dict[word] += 1
        else:
            word_counting_dict[word] = 1
            
for word in sorted(word_counting_dict.items(), key=lambda x: x[1], reverse=True)[:100]:
    print(word)

