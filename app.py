import os
import time
import logging
logging.basicConfig(level=logging.INFO)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(0.2)
    app.logger.info("Slept for 0.2 second")
    
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
