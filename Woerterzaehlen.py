#!/usr/bin/env python3

infile = open("newstest2009.de")

word_counter = 0

for line in infile:
    line = line.split()
    for word in line:
        word_counter = word_counter + 1
        # kürzer: word_counter += 1

print("Anzahl Wörter im Text:")
print(word_counter)
