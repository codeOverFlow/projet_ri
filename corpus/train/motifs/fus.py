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
    tmp = beatles & oasis
    for l in tmp:
        file_w.write(l)


with codecs.open('fusion/oasis_over_beatles.txt', 'w', 'utf-8') as file_w:
    tmp = beatles & oasis
    for l in tmp:
        file_w.write(l)


with codecs.open('fusion/beatles_over_metallica.txt', 'w', 'utf-8') as file_w:
    tmp = beatles & metallica
    for l in tmp:
        file_w.write(l)


with codecs.open('fusion/metallica_over_beatles.txt', 'w', 'utf-8') as file_w:
    tmp = beatles & metallica
    for l in tmp:
        file_w.write(l)


with codecs.open('fusion/beatles_over_all.txt', 'w', 'utf-8') as file_w:
    tmp = beatles & (oasis | metallica)
    for l in tmp:
        file_w.write(l)



with codecs.open('fusion/oasis_over_all.txt', 'w', 'utf-8') as file_w:
    tmp = oasis & (beatles | metallica)
    for l in tmp:
        file_w.write(l)


with codecs.open('fusion/metallica_over_all.txt', 'w', 'utf-8') as file_w:
    tmp = metallica & (beatles | oasis)
    for l in tmp:
        file_w.write(l)


