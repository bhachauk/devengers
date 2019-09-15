from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    html = '''
    <h2> Samsung Electronics Stock Prediction Prediction </h2>
    <h5>Predicted Value : </h5>
    <h5>46784.2532709241</h5>
    '''
    return html


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
