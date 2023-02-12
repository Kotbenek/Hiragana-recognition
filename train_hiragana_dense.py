import tensorflow as tf
import numpy as np
from common import *

input_dir = "unified_hiragana_no_small"
label_file = "hiragana_no_small_labels.txt"
output_dir = "models/dense"

REPEAT_COUNT = 10

def build_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(512, activation="relu", input_dim=train_data.shape[1]))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.Dense(512, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.Dense(256, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.Dense(71, activation="softmax"))

    model.summary()

    model.compile(loss=tf.keras.losses.categorical_crossentropy, optimizer=tf.keras.optimizers.Adam(learning_rate=0.0002), metrics=[tf.keras.metrics.CategoricalAccuracy()])

    return model

def train_model(train_data, train_labels, test_data, test_labels, output_dir):
    model = build_model()

    filepath = output_dir + "/model-{epoch:04d}-{val_categorical_accuracy:.4f}.h5"
    checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath, monitor='val_categorical_accuracy', verbose=1, save_best_only=True, mode='max')
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_categorical_accuracy', patience=20, verbose=1)
    callbacks_list = [checkpoint, early_stopping]

    return model.fit(train_data, train_labels, batch_size=128, epochs=1000000, callbacks=callbacks_list, verbose=1, validation_data=(test_data, test_labels))

if __name__ == "__main__":
    train_data, train_labels, test_data, test_labels = load_dataset(input_dir, label_file)

    train_data = train_data.reshape(-1, 64 * 64)
    test_data = test_data.reshape(-1, 64 * 64)

    for i in range(REPEAT_COUNT):
        od = f"{output_dir}{i}"
        history = train_model(train_data, train_labels, test_data, test_labels, od)
        plot_learning_curves(history, od)
