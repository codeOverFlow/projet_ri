#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import codecs
from os import listdir
from os.path import isfile, join

bo = [x.strip() for x in codecs.open('train/motifs/fusion/beatles_over_oasis.txt', 'r', 'utf-8').readlines()]
ob = [x.strip() for x in codecs.open('train/motifs/fusion/oasis_over_beatles.txt', 'r', 'utf-8').readlines()]
bm = [x.strip() for x in codecs.open('train/motifs/fusion/beatles_over_metallica.txt', 'r', 'utf-8').readlines()]
mb = [x.strip() for x in codecs.open('train/motifs/fusion/metallica_over_beatles.txt', 'r', 'utf-8').readlines()]
ba = [x.strip() for x in codecs.open('train/motifs/fusion/beatles_over_all.txt', 'r', 'utf-8').readlines()]
oa = [x.strip() for x in codecs.open('train/motifs/fusion/oasis_over_all.txt', 'r', 'utf-8').readlines()]
ma = [x.strip() for x in codecs.open('train/motifs/fusion/metallica_over_all.txt', 'r', 'utf-8').readlines()]

# 1
with codecs.open('ref/res_1', 'w', 'utf-8') as fi:
    onlyfiles = [join('motif_test/beatles',f) for f in listdir('motif_test/beatles') if isfile(join('motif_test/beatles',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bo])
        o = len([x for x in tmp if x in ob])
        if b > o:
            fi.write(f.split('/')[-1]+'\n')

    onlyfiles = [join('motif_test/oasis',f) for f in listdir('motif_test/oasis') if isfile(join('motif_test/oasis',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bo])
        o = len([x for x in tmp if x in ob])
        if b > o:
            fi.write(f.split('/')[-1]+'\n')
# 2
with codecs.open('ref/res_2', 'w', 'utf-8') as fi:
    onlyfiles = [join('motif_test/beatles',f) for f in listdir('motif_test/beatles') if isfile(join('motif_test/beatles',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bm])
        o = len([x for x in tmp if x in mb])
        if b > o:
            fi.write(f.split('/')[-1]+'\n')

    onlyfiles = [join('motif_test/metallica',f) for f in listdir('motif_test/metallica') if isfile(join('motif_test/metallica',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bm])
        o = len([x for x in tmp if x in mb])
        if b > o:
            fi.write(f.split('/')[-1]+'\n')   


# 3
with codecs.open('ref/res_3', 'w', 'utf-8') as fi:
    onlyfiles = [join('motif_test/beatles',f) for f in listdir('motif_test/beatles') if isfile(join('motif_test/beatles',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bo])
        bb = len([x for x in tmp if x in bm])
        o = len([x for x in tmp if x in ob])
        m = len([x for x in tmp if x in mb])
        if b > o and bb > m:
            fi.write(f.split('/')[-1]+'\n')

    onlyfiles = [join('motif_test/metallica',f) for f in listdir('motif_test/metallica') if isfile(join('motif_test/metallica',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bm])
        bb = len([x for x in tmp if x in bo])
        m = len([x for x in tmp if x in mb])
        o = len([x for x in tmp if x in ob])
        if bb > o and b > m:
            fi.write(f.split('/')[-1]+'\n')

    onlyfiles = [join('motif_test/oasis',f) for f in listdir('motif_test/oasis') if isfile(join('motif_test/oasis',f))]
    for f in onlyfiles:
        tmp = [x.split('\t')[0] for x in codecs.open(f, 'r', 'utf-8').readlines()]
        b = len([x for x in tmp if x in bm])
        bb = len([x for x in tmp if x in bo])
        m = len([x for x in tmp if x in mb])
        o = len([x for x in tmp if x in ob])
        if bb > o and b > m:
            fi.write(f.split('/')[-1]+'\n')
