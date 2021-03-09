
from config import var
import tensorflow as tf
from tensorflow import keras
import numpy as np

def non_gpu():
    data = np.asarray([[1,1],[1,0],[0,1],[0,0],[0,1],[1,1],[1,0],[0,1],[0,0],[0,1]])
    label = np.asarray([[1,0],[1,0],[1,0],[0,0],[1,0],[1,0],[1,0],[1,0],[0,0],[1,0]])
    ds = (data,label)

    model =  keras.Sequential()
    model.add(keras.layers.Dense(2,input_shape=(2,)))
    model.add(keras.layers.Dense(224, activation = 'relu'))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.Dense(2,activation="softmax"))

    model.compile(
        "Adam",
        loss = "mse",
        metrics = ["accuracy"]
    )
    model.summary()

    history = model.fit(data,label,epochs = 2000, validation_split=0.2, verbose = 0)
    var.check2 = False