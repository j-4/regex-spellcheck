#!/usr/bin/env python3

import re
import argparse
from termcolor import colored

try: input = raw_input
except NameError: pass

parser = argparse.ArgumentParser(description='Find common english mistakes with regex.')
parser.add_argument('file', metavar='FILE', type=str, nargs='+', help='Text file(s) to check')
parser.add_argument('--whitespace', '-w', action='store_true', help='Also detect whitespace issues')
parser.add_argument('--all', '-a', action='store_true', help='Print all matches at once without interaction')

args = parser.parse_args()

whitespacePattern = {
    r'(\s+)\1': r'\1',
    r'([;,\.?!])([A-Za-z]+)\b': r'\1 \2',
    r'\([\s]+': r'(',
    r'[\s]+\)': r')',
    r'\s+([:;,\.?!][A-Za-z])': r'\1'
}

grammarPattern = {
    r'\sa(\s[aeiou])': r' an\1',
    r'\san(\s[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])': r' a\1',
    r'(^[\.]\w\.\s)([a-z])': r'\1\2',
    r'\b(\w+)\s+\1\b': r'\1'
}

patterns = grammarPattern
if args.whitespace:
    patterns.update(whitespacePattern)


for filename in args.file:
    fcontent = ''
    with open(filename, 'r') as f:
        fcontent = f.read()

    for i, line in enumerate(fcontent.split('\n')):
        for expression, replacement in patterns.items():
            p = re.compile(expression, flags=0)
            mi = p.finditer(line)
            for m in mi:
                before = line[:m.span()[0]]
                after = line[m.span()[1]:]
                mistake = colored(m.group(0), 'red', attrs=['bold', 'underline'])
                print('{0:4d}: {1}{2}{3}'.format(i, before, mistake, after))
                r = colored(m.expand(replacement), 'blue', attrs=['bold', 'underline'])
                print('      {0}{1}{2}'.format(before, r, after))
                if not args.all:
                    c= input('')
                #c = raw_input('Replace with "' + r + '" [y/N]')
                #if c == 'Y':
                #    print('Replacement not implemented yet...')
