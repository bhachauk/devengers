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
print(next_test.index[0])

next_test.fillna(0, inplace=True)
print(next_test.head())

scaler = pickle.load(open("models/scaler.pkl", 'rb'))
test = scaler.transform(next_test)[0][:-1]

test = np.reshape(test, (1, 1, len(test)))

print('Model required Data :')
print(test)
# identical to the previous one
model = load_model('/media/bhanuchanderu/nova/dragon/devengers/models/GRU_4.h5')
predicted = model.predict(test)
print('predicted...')
print(predicted)

test = [-1] * input.shape[1]
test[(input.shape[1]-1)] = predicted[0][0]
actual_ans = scaler.inverse_transform([test])
print(actual_ans[0][input.shape[1]-1])
plt.plot(input['Close'])
plt.show()
