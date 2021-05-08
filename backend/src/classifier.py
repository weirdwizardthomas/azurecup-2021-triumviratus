import os

import numpy as np
from tensorflow import keras

from config import config
from image import INPUT_SHAPE

RELU = 'relu'
SOFTMAX = 'softmax'
PADDING = 'same'
DROPOUT = 0.2
STRIDE = (3, 3)
POOL_SIZE = (2, 2)
OPTIMIZER = 'Adam'
LOSS = 'categorical_crossentropy'
METRICS = ['accuracy']
CLASS_COUNT = config.classification.classes
MODEL_DIRECTORY = config.classification.model


class Classifier:
    __instance = None

    @staticmethod
    def get_instance():
        if Classifier.__instance is None:
            Classifier.__instance = Classifier()
        return Classifier.__instance

    def __init__(self):
        print(MODEL_DIRECTORY)
        self.model = keras.models.load_model(os.path.join(MODEL_DIRECTORY))
        self.classes = CLASS_COUNT

    def save_model(self, directory):
        self.model.save(directory)

    def predict(self, image):
        array = np.array(image).reshape(INPUT_SHAPE)
        batch = np.expand_dims(array, axis=0)
        predictions = self.model.predict(batch)[0]
        return dict(zip(self.classes, predictions))
