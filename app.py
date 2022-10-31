from flask import Flask,jsonify
from flask import request

import logging
import json

from trying import sentimentanalysis

app = Flask(__name__)



# @app.route("/",methods=["POST","GET"])
# def index():
#     return {"message":"Hello!"}

# line
@app.route("/sentiment",methods=["POST"])
def sentiment_expression():
    data = request.get_json()
    logging.info(data)
    result=sentimentanalysis(data)
    #result="testing sesion"
    print(result)
    logging.info(result)
    return jsonify(result)

# @app.route("/sent_analysis",methods=["POST"])
# def analyse_expression_upload():
#     file = request.files["file"]
#     actions = request.form.get("actions",DEFAULT_ACTIONS)
#     actions = json.loads(actions) if isinstance(actions,str) else actions
#     response = facial_analysis_with_file(file,actions)
#     return jsonify(response)



app.run(host="0.0.0.0",port=5003)