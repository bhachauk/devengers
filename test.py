# Template work
from pandas import read_csv
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import pickle


# details
index_col = 'Date'
target_col = 'Close'
final_target = 'target'


input = read_csv('data/train_with_nlp.csv')
input = input.set_index(index_col)
input = input.sort_index()
input = input.dropna()

input[final_target] = input[target_col].shift(-1)
next_test = input.tail(1)
input = input.dropna()

next_test.fillna(0, inplace=True)
print(next_test.values)

scaler = pickle.load(open("models/scaler.pkl", 'rb'))
test = scaler.transform(next_test)[0][:-1]

test = np.reshape(test, (1, 1, len(test)))
# identical to the previous one
models = []
models.append(('LSTM', load_model('models/LSTM_4.h5')))
models.append(('GRU', load_model('models/GRU_4.h5')))

for name, model in models:
    predicted = model.predict(test)
    temp = [-1] * input.shape[1]
    temp[(input.shape[1]-1)] = predicted[0][0]
    actual_ans = scaler.inverse_transform([temp])
    pred = actual_ans[0][input.shape[1] - 1]

    print(name + ' prediction : ' + str(pred))
    plt.scatter(x= len(input)+1, y =pred)
plt.plot(input['Close'])
plt.show()
