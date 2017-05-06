#!/usr/bin/env python3

import nltk

while True:
    sent = input("Write an english sentence or Q to quit: ")
    if sent == "Q":
        break
    else:
        sent = nltk.word_tokenize(sent)
        sent = nltk.pos_tag(sent, tagset="universal")
        print(sent)
