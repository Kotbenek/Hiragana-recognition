import os
from os.path import exists
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import tensorflow as tf

def quit_if_dir_exists(dir):
    if exists(dir):
        print(f"Directory '{dir}' already exists.")
        quit()

def mkdir(dir):
    os.mkdir(dir)

hiraganas = [
'あ', 'い', 'う', 'え', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ',
'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に',
'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま',
'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'
]

hiraganas_no_small = [
'あ', 'い', 'う', 'え', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ',
'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ',
'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み',
'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'
]

def hiragana_to_id(hiragana):
    # FIXME: support both hiraganas and hiraganas_no_small
    return hiraganas_no_small.index(hiragana)

def id_to_hiragana(id):
    # FIXME: support both hiraganas and hiraganas_no_small
    return hiraganas_no_small[id]

def find_bounding_box(image):
    x_size = image.size[0]
    y_size = image.size[1]

    pixels = image.load()

    boundary_left = -1
    boundary_right = -1
    boundary_top = -1
    boundary_bottom = -1

    #left
    for x in range(x_size):
        for y in range(y_size):
            if pixels[x, y] != 0:
                boundary_left = x
                break
        if boundary_left != -1:
            break

    #right
    for x in reversed(range(x_size)):
        for y in range(y_size):
            if pixels[x, y] != 0:
                boundary_right = x
                break
        if boundary_right != -1:
            break

    #top
    for y in range(y_size):
        for x in range(x_size):
            if pixels[x, y] != 0:
                boundary_top = y
                break
        if boundary_top != -1:
            break

    #bottom
    for y in reversed(range(y_size)):
        for x in range(x_size):
            if pixels[x, y] != 0:
                boundary_bottom = y
                break
        if boundary_bottom != -1:
            break

    return [boundary_left, boundary_right, boundary_top, boundary_bottom]

def unify_sample(image):
    x_size = image.size[0]
    y_size = image.size[1]

    x_size = max(x_size, y_size)
    y_size = max(x_size, y_size)

    bounding_box = find_bounding_box(image)

    sample = image.crop((bounding_box[0], bounding_box[2], bounding_box[1] + 1, bounding_box[3] + 1))

    sample_size_x = bounding_box[1] - bounding_box[0] + 1
    sample_size_y = bounding_box[3] - bounding_box[2] + 1

    if x_size - sample_size_x < y_size - sample_size_y:
        ratio = x_size / sample_size_x
    else:
        ratio = y_size / sample_size_y

    resized_sample = sample.resize((int(sample_size_x * ratio), int(sample_size_y * ratio)), resample=Image.Resampling.NEAREST)

    sample_size_x = resized_sample.size[0]
    sample_size_y = resized_sample.size[1]

    centered_left = (x_size - sample_size_x) // 2
    centered_top = (y_size - sample_size_y) // 2

    unified_sample = Image.new('L', (x_size, y_size), 0)
    unified_sample.paste(resized_sample, (centered_left,centered_top))

    return unified_sample

def load_dataset_samples(path):
    data = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            data.append([float(l.strip()) for l in line.rstrip()[1:-1].split(',')])
    return data

def load_dataset_labels(path):
    data = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            data.append(hiragana_to_id(line.rstrip()))
    return data

def read_data(input_dir):
    data = []
    for f in sorted(os.listdir(input_dir)):
        if os.path.isfile(f"{input_dir}/{f}") and f.endswith(".png"):
            with Image.open(f"{input_dir}/{f}") as image:
                x_size = image.size[0]
                y_size = image.size[1]
                pixels = image.load()
                sample = np.asarray(image) / 255
                data.append(sample)
    return data

def read_labels(label_file):
    labels = []
    with open(label_file, 'r') as f:
        for c in f.readline():
            labels.append(c)
    return labels

def split_data_into_train_and_test(data, labels):
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    i = 0
    j = 0
    for sample in data:
        if i < 150:
            train_data.append(sample)
            train_labels.append(hiragana_to_id(labels[j]))
        else:
            test_data.append(sample)
            test_labels.append(hiragana_to_id(labels[j]))
        i = (i + 1) % 160
        j = j + 1

    return np.array(train_data), tf.keras.utils.to_categorical(train_labels), np.array(test_data), tf.keras.utils.to_categorical(test_labels)

def load_dataset(input_dir, label_file):
    return split_data_into_train_and_test(read_data(input_dir), read_labels(label_file))

def plot_learning_curves(history, output_dir):
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(history.history['categorical_accuracy'])
    axs[0, 0].set_title('Accuracy (train)')
    axs[0, 0].set_xlabel('epoch')
    axs[0, 0].set_ylabel('accuracy')
    axs[0, 1].plot(history.history['val_categorical_accuracy'])
    axs[0, 1].set_title('Accuracy (val)')
    axs[0, 1].set_xlabel('epoch')
    axs[0, 1].set_ylabel('accuracy')
    axs[1, 0].plot(history.history['loss'])
    axs[1, 0].set_title('Loss (train)')
    axs[1, 0].set_xlabel('epoch')
    axs[1, 0].set_ylabel('loss')
    axs[1, 1].plot(history.history['val_loss'])
    axs[1, 1].set_title('Loss (val)')
    axs[1, 1].set_xlabel('epoch')
    axs[1, 1].set_ylabel('loss')

    for ax in axs.flat:
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    fig.tight_layout()

    plt.savefig(output_dir + "/fig.png")
