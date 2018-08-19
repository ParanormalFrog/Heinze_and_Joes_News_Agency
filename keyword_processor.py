# Takes in a keyword and turns it into a regular expression

import sys
import re


def generaliser():
    keyword = sys.argv[1:]
    keyword = " ".join(keyword).strip().upper()
    keyword = re.compile(r"" + str(keyword) + "([\'sS]{0,2})")
    return keyword
