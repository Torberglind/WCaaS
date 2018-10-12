from celery import Celery

import os
import json
import re

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

app.config_from_object('celeryconfig')

@app.task
def count():
    wordcounter = ["han", "hon", "den", "det", "denne", "denna", "hen"]
    dictpronoun = {}
    for pronoun in wordcounter:
        dictpronoun[pronoun] = 0
    dirpath = './data'
    tweet_counter = 0
    for file in os.listdir(dirpath):
        filepath = dirpath + "/" + file
        with open (filepath, 'r') as tweet:
            for line in tweet:
                try:
                    tweet = json.loads(line)
                except ValueError:
                    continue
                if ('retweeted_status' in tweet):
                    continue
                else:
                    regex = [r'\bhan\b', r'\bhon\b', r'\bden\b', r'\bdet\b', r'\bdenne\b', r'\bdenna\b', r'\bhen\b']
                    tweet_counter = tweet_counter + 1
                    text = tweet['text']
                    for x in regex:
                        found = re.findall(x, text, re.IGNORECASE)
                        if found:
                            dictpronoun[x[2:-2]]+=1

    return (dictpronoun)