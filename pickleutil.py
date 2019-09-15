import pickle


def get_transformed(test):
    scaler = pickle.load(open("models/scaler.pkl", 'rb'))
    return scaler.transform(test)