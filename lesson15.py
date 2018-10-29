#!/user/bin/env python3
# -*- coding: utf-8 -*-

"fishzz's module"

__author__ = 'fishzz'

import sys
from PIL import Image


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello, world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('too many arguments!')


if __name__ == "__main__":
    test()
