from flask import Flask
from flask import request
import pickleutil as pu
app = Flask(__name__)


@app.route("/")
def hello():
    html = '''
    <div align="center">
    <h1 style="color:blue;"> Samsung Electronics Stock Prediction Prediction </h1>
    <h3 >Predicted Value : </h3>
    <h5 style="color:red;">GRU : 46784.2532709241</h5>
    <h5 style="color:red;">LSTM : 46699.87167716027</h5>
    </div>
    
    <div align="center">
        <h3 >Trend</h3>
        <img src="https://raw.githubusercontent.com/Bhanuchander210/devengers/master/outputs/final.png"/>
    </div>
    
    <h3 >Techniques Used</h3>
    <ul>
        <li>Recurrent Neural Network</li>
        <li>NLP</li>
    </ul>
    
    <h3>Observation</h3>
    <h3>GRU</h3>
    <h5>Loss : 0.176</h5>
    <h5>Loss / Learning Trend</h5>
    <img src="https://raw.githubusercontent.com/Bhanuchander210/devengers/master/outputs/gru_4.png"></img>
    
    <h3>LSTM</h3>
    <h5>Loss : 0.172</h5>
    <h5>Loss / Learning Trend</h5>
    <img src="https://raw.githubusercontent.com/Bhanuchander210/devengers/master/outputs/lstm_4.png"></img>
    
    <h2>To Predict the current / Intra day prediction checkout 'test.py' GitHub:</h2>
    <a href="https://github.com/Bhanuchander210/devengers">Link</a>
    '''
    return html


@app.route("/predict")
def predict():
    loaded = request.args.get('input')
    loaded = list([ float(x) for x in str(loaded).split(',')])
    test = loaded.append(0)
    scaled = pu.get_transformed(test)
    return "hi"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
