import numpy as np
from tensorflow import keras

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
CLASS_COUNT = 9


class Classifier:
    __instance = None

    @staticmethod
    def get_instance(model_directory, classes):
        if Classifier.__instance is None:
            Classifier.__instance = Classifier(model_directory, classes)
        return Classifier.__instance

    def __init__(self, model_directory, classes):
        self.model = keras.models.load_model(model_directory)
        self.classes = classes

    def save_model(self, directory):
        self.model.save(directory)

    def predict(self, image):
        array = np.array(image).reshape(INPUT_SHAPE)
        batch = np.expand_dims(array, axis=0)
        predictions = self.model.predict(batch)[0]
        return dict(zip(self.classes, predictions))
