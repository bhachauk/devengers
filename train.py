# Template work

from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, GRU
import matplotlib.pyplot as plt
import numpy as np
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


scaler = MinMaxScaler(feature_range=(-1, 1))
values = scaler.fit_transform(input.values)
pickle.dump(scaler, open("models/scaler.pkl", 'wb'))

train = values
test = values

print('Training data length : ', len(train))
print('Test data length : ', len(test))

# split into input and outputs
trainX, trainY = train[:, :-1], train[:, -1]
testX, testY = test[:, :-1], test[:, -1]

input_col_len = len(trainX[0])

trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))


def gru(n):
    model = Sequential()
    model.add(GRU(n, input_shape=(1, input_col_len)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def lstm(n):
    model = Sequential()
    model.add(LSTM(n, input_shape=(1, input_col_len)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def plot_history(history, name):
    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.title('{} Model loss'.format(name))
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train'], loc='upper left')
    plt.show()


models = list()
models.append(('GRU_4', gru(4)))
# models.append(('GRU_8', gru(8)))
# models.append(('GRU_12', gru(12)))
# models.append(('GRU_16', gru(16)))
models.append(('LSTM_4', lstm(4)))
# models.append(('LSTM_8', lstm(8)))
# models.append(('LSTM_12', lstm(12)))
# models.append(('LSTM_16', lstm(16)))
results = []
# This is the actual value got

for model_name, model in models:

    start_time = time.time()

    history = model.fit(trainX, trainY, epochs=40, batch_size=1, verbose=1)

    # print history.history.keys()
    plot_history(history, model_name)

    print("[INFO] Model : {} Training done...".format(model_name))
    print("[INFO] Data Training time is :  %s s" % (time.time() - start_time))
    print (history.params)
    print(model.summary())
    model.save('models/'+model_name+'.h5')

    # make predictions
    # trainPredict = model.predict(trainX)
    # print (trainPredict)



