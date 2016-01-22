#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import codecs

b = codecs.open('resultat_beatles.txt', 'r', 'utf-8')
o = codecs.open('resultat_oasis.txt', 'r', 'utf-8')
m = codecs.open('resultat_metallica.txt', 'r', 'utf-8')

beatles = set([x.split('\t')[0] for x in b.readlines()])
oasis = set([x.split('\t')[0] for x in o.readlines()])
metallica = set([x.split('\t')[0] for x in m.readlines()])

b.close()
o.close()
m.close()

with codecs.open('fusion/beatles_over_oasis.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in beatles if x not in oasis]
    for l in tmp:
        file_w.write(l+'\n')


with codecs.open('fusion/oasis_over_beatles.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in oasis if x not in beatles]
    for l in tmp:
        file_w.write(l+'\n')


with codecs.open('fusion/beatles_over_metallica.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in beatles if x not in metallica]
    for l in tmp:
        file_w.write(l+'\n')


with codecs.open('fusion/metallica_over_beatles.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in metallica if x not in beatles]
    for l in tmp:
        file_w.write(l+'\n')


with codecs.open('fusion/beatles_over_all.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in beatles if x not in oasis and x not in metallica]
    for l in tmp:
        file_w.write(l+'\n')



with codecs.open('fusion/oasis_over_all.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in oasis if x not in beatles and x not in metallica]
    for l in tmp:
        file_w.write(l+'\n')


with codecs.open('fusion/metallica_over_all.txt', 'w', 'utf-8') as file_w:
    tmp = [x for x in metallica if x not in oasis and x not in beatles]
    for l in tmp:
        file_w.write(l+'\n')


