from flask import Flask
from shipment.logger import logging

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info ('we are just testing the loging module')

    return 'Hello Mukul you are start the modular coding'

if __name__ == '__main__':
    app.run(debug=True)
    