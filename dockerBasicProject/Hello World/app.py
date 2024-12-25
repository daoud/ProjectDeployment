## flask app for hello world
##https://www.youtube.com/watch?v=8vmKtS8W7IQ

from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)