# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import logging
import csv
import re
import operator
import pickle

# <codecell>

# Logging definition
logger = logging.getLogger('processing')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('log/process_ngrams.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# <headingcell level=3>

# NLP analysis

# <codecell>

# Load Sentiwordnet
sentiwordnet = {}
with open('data/sentiwordnet/sentiwordnet.tsv', 'rb') as ifile:
    reader = csv.reader(ifile , delimiter='\t')
    headers = reader.next()
    for row in reader:
        # Upload only adjectives and with a specific objectivity threshold
        cond1 = row[2] == "a"
        if cond1:
            sentiwordnet["%s" % (row[5])] = {"pos": float(row[6]), "neg": float(row[7]), "obj": 1.0, 
                                             "regex": re.compile('(\s\S+){0,%s} (%s)(\s\S+){0,%s}' % (3, row[5] ,3) , re.IGNORECASE)}
logger.info(' %s sentiwords loaded.' % (len(sentiwordnet)))

# <codecell>

# Process each review and generate coocurrences matrix
words_labels = {}

review_number = 0
with open('data/amazon/Cell_Phones_&_Accessories.txt', 'rb') as ifile:
    with open('data/output/words_labeled.p', 'wb') as ofile:
        # Write header
        ofile.write("word\tpos\tneg\tlabel\n")                                 
        review = ""
        score = 0
        for line in ifile.readlines():
            # Review Processing
            if "product/productId" in line and len(review) > 0:
                chunks = re.split(';|,|\\.|\\*|\\n', review)
                for chunk in chunks:
                    for w in sentiwordnet:
                        for match in sentiwordnet[w]["regex"].finditer(chunk):
                            #ofile.write("%s\t%s\t%s\t%s\t\n" % (w, sentiwordnet[w]["pos"], sentiwordnet[w]["neg"], score))
                            if w not in words_labels:
                                words_labels[w] = {"1.0": 0, "2.0": 0, "3.0": 0, "4.0": 0, "5.0": 0}
                            words_labels[w][str(score)] += 1
                # Clean review content
                review = ""
                # Debug info
                if review_number % 500 == 0:
                    logger.info(' Reviews proccesed: %s Word detected: %s' % (review_number, len(words_labels)))
                    # Incremental saving
                    pickle.dump(words_labels, ofile)
                    if review_number == 500:
                        break
                review_number += 1
            # Add score
            if "review/score" in line:
                score = float(line[len(line)-4:len(line)])
            # Add line to review
            if "review/text" in line:
                review += line       
logger.info(' Saved %s words labeled.' % (len(words_labels))) 

# <codecell>


