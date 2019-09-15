from flask import Flask
from keras.models import load_model
from flask import request
import pickle, numpy as np
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hi there... Itachi here...!"


@app.route("/predict")
def predict():
    open = request.args.get('open')
    high = request.args.get('high')
    low = request.args.get('low')
    volume = request.args.get('volume')
    open_aapl = request.args.get('open_aapl')
    high_aapl = request.args.get('high_aapl')
    low_aapl = request.args.get('low_aapl')
    open_goog = request.args.get('open_goog')
    high_goog = request.args.get('high_goog')
    low_goog = request.args.get('low_goog')
    open_intc = request.args.get('open_intc')
    high_intc = request.args.get('high_intc')
    low_intc = request.args.get('low_intc')
    open_lg = request.args.get('open_lg')
    high_lg = request.args.get('high_lg')
    low_lg = request.args.get('low_lg')
    sentiment = request.args.get('sentiment')
    subjectivity = request.args.get('subjectivity')

    test = [open,high,low,volume,open_aapl,high_aapl,low_aapl,open_goog,high_goog,low_goog,open_intc,high_intc, low_intc,open_lg, high_lg, low_lg, sentiment, subjectivity, 0]
    scaler = pickle.load(open("models/scaler.pkl", 'rb'))
    test = scaler.transform(test)[0][:-1]
    test = np.reshape(test, (1, 1, len(test)))
    model = load_model('models/GRU_4.h5')
    predicted = model.predict(test)
    return str(predicted)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)