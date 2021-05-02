from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.constraints import maxnorm
from keras.layers.convolutional import Conv2D, MaxPooling2D

RELU = 'relu'
SOFTMAX = 'softmax'
PADDING = 'same'
DROPOUT = 0.2
STRIDE = (3,3)
POOL_SIZE = (2,2)

def get_model(width, height, channels = 1, optimizer = 'Adam', loss = 'categorical_crossentropy'):
    input_shape = (width, height, channels)

    model = Sequential()

    model.add(Conv2D(32, STRIDE, input_shape = input_shape, padding=PADDING))
    model.add(Activation(RELU))
    model.add(Dropout(DROPOUT))
    model.add(BatchNormalization())

    model.add(Conv2D(64, STRIDE, padding=PADDING))
    model.add(Activation(RELU))
    model.add(MaxPooling2D(pool_size=POOL_SIZE))
    model.add(Dropout(DROPOUT))
    model.add(BatchNormalization())

    model.add(Conv2D(64, STRIDE, padding=PADDING))
    model.add(Activation(RELU))
    model.add(MaxPooling2D(pool_size=POOL_SIZE))
    model.add(Dropout(DROPOUT))
    model.add(BatchNormalization())

    model.add(Conv2D(128, STRIDE, padding=PADDING))
    model.add(Activation(RELU))
    model.add(Dropout(DROPOUT))
    model.add(BatchNormalization())

    model.add(Flatten())
    model.add(Dropout(DROPOUT))

    model.add(Dense(256, kernel_constraint=maxnorm(3)))
    model.add(Activation(RELU))
    model.add(Dropout(DROPOUT))
    model.add(BatchNormalization())

    model.add(Dense(128, kernel_constraint=maxnorm(3)))
    model.add(Activation(RELU))
    model.add(Dropout(DROPOUT))
    model.add(BatchNormalization())

    model.add(Dense(9))
    model.add(Activation(SOFTMAX))

    model.compile(loss = loss, optimizer = optimizer, metrics=['accuracy'])

    return model

def save_model(model, directory):
    model.save(directory)

def load_model(directory):
    return keras.models.load_model(directory)   