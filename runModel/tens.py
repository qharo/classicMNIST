#------MODULES------#
import time
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
#------------#

def predict(grid): #PREDICTION FUNCTION LOADS UP AN ALREADY TRAINED MODEL
    grid = np.array(grid)
    grid.reshape(28,28,1)    
    grid = grid.reshape(list(grid.shape) + [1])
    print(grid.shape)
    model = create_model()
    model.load_weights('trainedModel/cp.ckpt')
    model.summary()
    prediction = model.predict([grid])
    return str(np.argmax(prediction))

def create_model(): #CREATES A MODEL LIKE THE PREVIOUSLY TRAINED ONE, TO WHICH THE WEIGHTS ARE LOADED
    model = keras.Sequential([
      keras.layers.Conv2D(16, (3,3), activation='relu', input_shape = (28,28,1)),
      keras.layers.MaxPool2D(2,2),
      keras.layers.Conv2D(32, (3,3), activation="relu"), 
      keras.layers.MaxPool2D(2,2),
      keras.layers.Conv2D(64, (3,3), activation="relu"),
      keras.layers.Conv2D(128, (3,3), activation="relu"),
      keras.layers.Flatten(),
      keras.layers.Dense(64, activation='relu'),
      keras.layers.Dense(32, activation='relu'),
      keras.layers.Dense(16, activation='relu'),
      keras.layers.Dense(10),                       
    ])

    model.compile(
        optimizer='adam', 
        loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'],
        )
    return model
