#!/usr/bin/env python3

from nltk import word_tokenize

infile = open("newstest2009.de", encoding="utf-8")

token_counter = 0

for line in infile:
    line = word_tokenize(line)
    for token in line:
        token_counter = token_counter + 1
        # kürzer: token_counter += 1

print("Anzahl Wörter im Text:")
print(token_counter)

infile.close()
