from flask import Flask

from adaptivedetector import adaptive
from contentdetector import contentdet


from thresholddetector import thresholdDetector

app=Flask(__name__)

@app.route("/extract",methods=["GET","POST"])
def extractScene():
    adaptive("../resource/Sample.mp4")
    # ttryy("resource/chunk8.mp4")
    # thresholdDetector("../resource/Sample.mp4")
    return 'success'

app.run(port=8098)
