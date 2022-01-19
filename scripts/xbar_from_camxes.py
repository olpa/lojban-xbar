#!/usr/bin/env python3

import json
import os
import sys

if 'LOJBAN_XBAR_DEVEL' in os.environ:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from lojban_xbar import camxes_to_lcs

def print_help():
    print("Convert camxes parse tree to XBar")
    print(f"$ camxes.py 'mi klama' | {__file__} | xbar_to_dot.py >xbar.dot")

def main():
    camxes_tree = json.load(sys.stdin)
    lcs_tree = camxes_to_lcs(camxes_tree)
    json.dump(lcs_tree, sys.stdout)
    print('')

if '-' in sys.argv or '--help' in sys.argv:
    print_help()
else:
    main()
