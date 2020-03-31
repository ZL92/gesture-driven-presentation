# import xmltodict
import numpy as np
# import os

from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from xml_processing_tools import *


def evaluate_model(trainX, trainy, testX, testy):
    verbose, epochs, batch_size = 0, 15, 64
    n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]  # 128, 9, 6
    model = Sequential()
    model.add(LSTM(100, input_shape=(n_timesteps, n_features)))
    model.add(Dropout(0.5))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose)
    # evaluate model
    _, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=0)
    return accuracy



X,Y = xmlToNumpy()

repeats = 2
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
scores = list()
for r in range(repeats):
    score = evaluate_model(X_train, y_train, X_test, y_test)
    score = score * 100.0
    print('>#%d: %.3f' % (r + 1, score))
    scores.append(score)

debug(scores)
# summarize_results(scores)