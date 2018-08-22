# Takes in a keyword and turns it into a regular expression
import os
import sys
import re



def generaliser(keyword):
    keyword = keyword
    keyword = keyword.strip().upper()
    keyword = "\n" + str(keyword) + "([\'sS]{0,2})"
    file = open('./utility/test.file.txt', mode='a+')
    file.write(keyword)
    return keyword