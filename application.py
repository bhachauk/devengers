from flask import Flask
from keras.models import load_model
import pickle
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, SmartNinja!"


@app.route("/test")
def test(inval):
    return "this is our inval ; " + inval


@app.route("/predict")
def newhello():
    test = []
    model = load_model('models/GRU_4.h5')
    predicted = model.predict(test)
    return str(predicted)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)