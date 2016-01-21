#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import treetaggerwrapper
from nltk.corpus import stopwords

seq = []
with codecs.open(sys.argv[1], 'r', 'utf8') as file_r:
	lines = file_r.readlines()
	for line in lines:
		seq.append(line.strip()+' .')


# Construction et configuration du wrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='TreeTagger',
TAGINENC='utf-8',TAGOUTENC='utf-8')
# Utilisation
for l in seq:
	for ll in tagger.TagText(l):
		s = ll.split('\t')
		s = [t.lower() for t in s]
		if not s[0] == s[1] and not s[0] in stopwords.words('english'):
			print '\t'.join(s)
