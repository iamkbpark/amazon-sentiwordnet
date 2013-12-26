# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import logging
import pickle
import numpy as np
from __future__ import division 

# <codecell>

# Logging definition
logger = logging.getLogger('analyzing')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('log/process_ngrams.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# <codecell>

def normalize(value):
    """
    Normalize % value to 0.0<=value<=1.0
    """
    value = float(value)
    if value > 1.0:
        return value / 100
    else:
        return value
    
# Load Sentiwordnet
sentiwordnet = {}
with open('data/sentiwordnet/sentiwordnet.tsv', 'rb') as ifile:
    reader = csv.reader(ifile , delimiter='\t')
    headers = reader.next()
    for row in reader:
        # Upload only adjectives and with a specific objectivity threshold
        cond1 = True
        if cond1:
            sentiwordnet["%s" % (row[5])] = {"pos": normalize(row[6]), "neg": normalize(row[7]), "obj": 1.0}
logger.info(' %s sentiwords loaded' % (len(sentiwordnet)))

# <codecell>

# Process each review
total_bands = {"1.0": 0, "2.0": 0, "3.0": 0, "4.0": 0, "5.0": 0}

with open('data/output/words_labeled.p', 'rb') as ifile:
    words = pickle.loads(ifile.read())
    logger.info(' %s labeled words loaded' % (len(words)))
    with open('data/output/results.tsv', 'wb') as ofile:
        writer = csv.writer(ofile, delimiter='\t')
        writer.writerow(["word", "pos", "neg", "1.0", "2.0", "3.0", "4.0", "5.0"])
                            
        for word in words:
            for band in words[word]:
                total_bands[band] += words[word][band]
            n = sum(words[word][i] for i in words[word])

            # Random experiment
            random_experiment = False
            if not random_experiment:
                sw_pos = sentiwordnet[word]["pos"]
                sw_neg = sentiwordnet[word]["neg"]
            else:
                if np.random.uniform(0,1) > 0.5:
                    sw_pos = 0.0
                    sw_neg = np.random.uniform(0,1)
                else:
                    sw_neg = 0.0
                    sw_pos = np.random.uniform(0,1)
                    
            # Write row to file
            writer.writerow([word, sw_pos, sw_neg, 
                            words[word]["1.0"]/n, words[word]["2.0"]/n, words[word]["3.0"]/n, 
                            words[word]["4.0"]/n, words[word]["5.0"]/n])

logger.info(' Bands distribution %s' % (total_bands))       

# <headingcell level=3>

# Bands probability Analysis 

# <codecell>

def acum_probability(data, bands):
    """
    Return accum probability
    """
    n = sum(data[band] for band in data)
    if n == 0:
        return 0.0
    else:
        return sum([data[band]/n for band in bands])
        
    
with open('data/output/words_labeled.p', 'rb') as ifile:
    words = pickle.load(ifile)
    for word in words:
        value = acum_probability(words[word], ["3.0", "4.0", "5.0"])
        if value >= 0.9:
            pass
            print(word," ",words[word])

# <codecell>

total_bands = {"1.0": 0, "2.0": 0, "3.0": 0, "4.0": 0, "5.0": 0}
with open('data/amazon/Cell_Phones_&_Accessories.txt', 'rb') as ifile:
    for line in ifile.readlines():
        if "review/score" in line:
            score = float(line[len(line)-4:len(line)])
            total_bands[str(score)] += 1
print(total_bands)

# <codecell>


