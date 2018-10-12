#!flask/bin/python
from tasks import count

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/WCaaS/api/v1.0/count', methods=['GET'])
def WCaaS():
    result = count.delay()
    return jsonify((result.get()))

"""
@app.route('/WCaaS/api/v1.0/visualize', method ['GET'])
def WCVaaS():
    count_data = WCaaS()
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)