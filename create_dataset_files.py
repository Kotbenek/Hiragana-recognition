from PIL import Image
from common import *

input_dir = "unified_hiragana"
output_dir = "hiragana_dataset"

label_dir = "extracted"
label_files = [
"ETL8B2C1_00.txt", "ETL8B2C1_01.txt", "ETL8B2C1_02.txt", "ETL8B2C1_03.txt", "ETL8B2C1_04.txt",
"ETL8B2C1_05.txt"
]

def read_data():
    data = []
    for f in sorted(os.listdir(input_dir)):
        if os.path.isfile(f"{input_dir}/{f}") and f.endswith(".png"):
            with Image.open(f"{input_dir}/{f}") as image:
                x_size = image.size[0]
                y_size = image.size[1]
                pixels = image.load()
                sample = []
                for y in range(y_size):
                    for x in range(x_size):
                        sample.append(pixels[x, y] / 255)                
                data.append(sample)
    return data

def read_labels():
    labels = []
    for label_file in label_files:
        with open(f"{label_dir}/{label_file}", 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                for c in line.strip():
                    labels.append(c)
    return labels

def write_dataset_150_10(data, labels):
    local_output_dir = f"{output_dir}/150_10"
    mkdir(local_output_dir)

    with open(f"{local_output_dir}/train.txt", 'w') as f_train, \
         open(f"{local_output_dir}/train_labels.txt", 'w') as f_train_labels, \
         open(f"{local_output_dir}/test.txt", 'w') as f_test, \
         open(f"{local_output_dir}/test_labels.txt", 'w') as f_test_labels:
        i = 0
        j = 0
        for sample in data:
            if i < 150:
                f_train.write(f"{sample}\n")
                f_train_labels.write(f"{labels[j]}\n")
            else:
                f_test.write(f"{sample}\n")
                f_test_labels.write(f"{labels[j]}\n")
            i = (i + 1) % 160
            j = j + 1

def write_dataset_140_10_10(data, labels):
    local_output_dir = output_dir + "/" + "140_10_10"
    mkdir(local_output_dir)

    with open(f"{local_output_dir}/train.txt", 'w') as f_train, \
         open(f"{local_output_dir}/train_labels.txt", 'w') as f_train_labels, \
         open(f"{local_output_dir}/test.txt", 'w') as f_test, \
         open(f"{local_output_dir}/test_labels.txt", 'w') as f_test_labels, \
         open(f"{local_output_dir}/validation.txt", 'w') as f_validation, \
         open(f"{local_output_dir}/validation_labels.txt", 'w') as f_validation_labels:
        i = 0
        j = 0
        for sample in data:
            if i < 140:
                f_train.write(f"{sample}\n")
                f_train_labels.write(f"{labels[j]}\n")
            elif i < 150:
                f_test.write(f"{sample}\n")
                f_test_labels.write(f"{labels[j]}\n")
            else:
                f_validation.write(f"{sample}\n")
                f_validation_labels.write(f"{labels[j]}\n")
            i = (i + 1) % 160
            j = j + 1

if __name__ == "__main__":
    quit_if_dir_exists(output_dir)
    mkdir(output_dir)
    write_dataset_150_10(read_data(), read_labels())
    write_dataset_140_10_10(read_data(), read_labels())

