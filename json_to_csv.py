'''
Convert Yelp Academic Dataset from JSON to CSV
https://github.com/tothebeat/Yelp-Challenge-Dataset/blob/master/convert.py
By Paul Butler, No Rights Reserved
'''
import json
import sys

import pandas as pd
from glob import glob

filename = sys.argv[1]
# 'big_yelp_data/business.json'

def convert(x):
    ''' Convert a json string to a flat python dictionary
    which can be passed into Pandas. '''
    ob = json.loads(x)
    newob = dict(ob)
    for k, v in ob.items():
        if isinstance(v, list):
            newob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                newob['%s_%s' % (k, kk)] = vv
            del newob[k]
    return newob


for json_filename in glob(filename):
    csv_filename = '%s.csv' % json_filename[:-len('.json')]
    print('Converting %s to %s' % (json_filename, csv_filename))
    f = open(json_filename, "r")
    df = pd.DataFrame([convert(line) for line in f])
    df.to_csv(csv_filename, encoding='utf-8', index=False)

