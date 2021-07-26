import logging
from datetime import datetime  


from flask import Flask
from flask import Response

app = Flask(__name__)


logging.basicConfig(filename = 'app.log',format='%(asctime)s - %(message)s', level=logging.DEBUG)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():

    logging.debug("status endpoint was reached")

    return Response("""{"result":"0K- healthy"}""", status = 200, mimetype= 'application/json')

    

    

@app.route("/metrics")
def metrics():

    logging.debug("metrics endpoint was reached")

    return Response("""{"UserCount": 140, "UserCountActive": 23}""",status = 200, mimetype= 'application/json')




if __name__ == "__main__":
    app.run(host='0.0.0.0')
