from keras.constraints import maxnorm
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from tensorflow import keras

from src.image import INPUT_SHAPE

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
    def get_instance(create_new=True, directory=None, input_shape=INPUT_SHAPE, class_count=CLASS_COUNT):
        if Classifier.__instance is None:
            Classifier.__instance = Classifier(input_shape) if create_new else Classifier.load_model(directory)
        return Classifier.__instance

    def __init__(self, input_shape=(256, 256, 1), optimizer=OPTIMIZER, loss=LOSS, class_count=CLASS_COUNT):
        self.model = Sequential()

        self.model.add(Conv2D(32, STRIDE, input_shape=input_shape, padding=PADDING))
        self.model.add(Activation(RELU))
        self.model.add(Dropout(DROPOUT))
        self.model.add(BatchNormalization())

        self.model.add(Conv2D(64, STRIDE, padding=PADDING))
        self.model.add(Activation(RELU))
        self.model.add(MaxPooling2D(pool_size=POOL_SIZE))
        self.model.add(Dropout(DROPOUT))
        self.model.add(BatchNormalization())

        self.model.add(Conv2D(64, STRIDE, padding=PADDING))
        self.model.add(Activation(RELU))
        self.model.add(MaxPooling2D(pool_size=POOL_SIZE))
        self.model.add(Dropout(DROPOUT))
        self.model.add(BatchNormalization())

        self.model.add(Conv2D(128, STRIDE, padding=PADDING))
        self.model.add(Activation(RELU))
        self.model.add(Dropout(DROPOUT))
        self.model.add(BatchNormalization())

        self.model.add(Flatten())
        self.model.add(Dropout(DROPOUT))

        self.model.add(Dense(256, kernel_constraint=maxnorm(3)))
        self.model.add(Activation(RELU))
        self.model.add(Dropout(DROPOUT))
        self.model.add(BatchNormalization())

        self.model.add(Dense(128, kernel_constraint=maxnorm(3)))
        self.model.add(Activation(RELU))
        self.model.add(Dropout(DROPOUT))
        self.model.add(BatchNormalization())

        self.model.add(Dense(class_count))
        self.model.add(Activation(SOFTMAX))

        self.model.compile(loss=loss, optimizer=optimizer, metrics=METRICS)

    def save_model(self, directory):
        self.model.save(directory)

    @staticmethod
    def load_model(directory):
        return keras.models.load_model(directory)

    def predict(self, image):
        ...
