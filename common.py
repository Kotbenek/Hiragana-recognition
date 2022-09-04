import os
from os.path import exists
import pickle

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

def hiragana_to_id(hiragana):
    return hiraganas.index(hiragana)

def id_to_hiragana(id):
    return hiraganas[id]

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

def dump_obj_to_file(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load_obj_from_file(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

