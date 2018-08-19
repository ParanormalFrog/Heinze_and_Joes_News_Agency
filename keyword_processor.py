# Takes in a keyword and turns it into a regular expression
import os
import sys
import re

file = open(os.getcwd()+"/test.file.txt", mode='a+')


def generaliser():
    keyword = sys.argv[1:]
    keyword = " ".join(keyword).strip().upper()
    keyword = "\n" + str(keyword) + "([\'sS]{0,2})"
    return keyword

file.write(generaliser())
