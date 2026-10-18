import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    for character, frequency in result[:3]:
        print(character, frequency)
