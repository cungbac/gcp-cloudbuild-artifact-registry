import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    myEnvVar = os.environ.get('envVar')
    return 'I have changed the text here for testing: {}!\n second line'.format(myEnvVar)

if __name__ == '__main__':
    print('Starting app ...')
    app.debug = True
    app.host = '0.0.0.0'
    app.port = int(os.environ.get('PORT',8080))
    app.run()
