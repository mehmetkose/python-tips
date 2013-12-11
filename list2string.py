#!/usr/bin/env python
#-*- coding:utf-8 -*-

liste = ["tag1","tag2","tag3"]

# this style is more faster than + operator
merged = ", ".join([item for item in liste])

# elma, ali, armut
print merged