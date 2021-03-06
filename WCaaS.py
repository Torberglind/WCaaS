#!flask/bin/python
from tasks import count, sumdict
import os
from flask import Flask, jsonify
from celery import chord
from datetime import datetime

app = Flask(__name__)

@app.route('/WCaaS/api/v1.0/count', methods=['GET'])
def WCaaS():
    """
    result = count.delay()
    return jsonify((result.get()))
    """
    start = datetime.today()
    print (start)
    header = []
    dirpath = '../data'
    for file in os.listdir(dirpath):
        filepath = dirpath + "/" + file
        header.append(count.s(filepath))

    callback = sumdict.s()
    result = chord(header)(callback)
    ret = jsonify(result.wait())
    stop = datetime.today()
    print (stop - start)
    return ret




"""
@app.route('/WCaaS/api/v1.0/visualize', method ['GET'])
def WCVaaS():
    count_data = WCaaS()
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
