#!/usr/bin/env python
#-*- coding:utf-8 -*-

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


f = open('categories.txt')
for piece in read_in_chunks(f):
    print "\n you noooo work \n "+piece+"\n you nooooooo work \n "