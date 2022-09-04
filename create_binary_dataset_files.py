from common import *

input_dir = "hiragana_dataset"
output_dir = "binary_dataset"

def create_binary_files_150_10():
    local_input_dir = input_dir + "/" + "150_10"
    local_output_dir = output_dir + "/" + "150_10"
    mkdir(local_output_dir)

    test_samples = load_dataset_samples(local_input_dir + "/" + "test.txt")
    test_labels = load_dataset_labels(local_input_dir + "/" + "test_labels.txt")
    train_samples = load_dataset_samples(local_input_dir + "/" + "train.txt")
    train_labels = load_dataset_labels(local_input_dir + "/" + "train_labels.txt")

    dump_obj_to_file(test_samples, local_output_dir + "/" + "test_samples.bin")
    dump_obj_to_file(test_labels, local_output_dir + "/" + "test_labels.bin")
    dump_obj_to_file(train_samples, local_output_dir + "/" + "train_samples.bin")
    dump_obj_to_file(train_labels, local_output_dir + "/" + "train_labels.bin")

def create_binary_files_140_10_10():
    local_input_dir = input_dir + "/" + "140_10_10"
    local_output_dir = output_dir + "/" + "140_10_10"
    mkdir(local_output_dir)

    test_samples = load_dataset_samples(local_input_dir + "/" + "test.txt")
    test_labels = load_dataset_labels(local_input_dir + "/" + "test_labels.txt")
    train_samples = load_dataset_samples(local_input_dir + "/" + "train.txt")
    train_labels = load_dataset_labels(local_input_dir + "/" + "train_labels.txt")
    validation_samples = load_dataset_samples(local_input_dir + "/" + "validation.txt")
    validation_labels = load_dataset_labels(local_input_dir + "/" + "validation_labels.txt")

    dump_obj_to_file(test_samples, local_output_dir + "/" + "test_samples.bin")
    dump_obj_to_file(test_labels, local_output_dir + "/" + "test_labels.bin")
    dump_obj_to_file(train_samples, local_output_dir + "/" + "train_samples.bin")
    dump_obj_to_file(train_labels, local_output_dir + "/" + "train_labels.bin")
    dump_obj_to_file(validation_samples, local_output_dir + "/" + "validation_samples.bin")
    dump_obj_to_file(validation_labels, local_output_dir + "/" + "validation_labels.bin")

def create_binary_files():
    create_binary_files_150_10()
    create_binary_files_140_10_10()

if __name__ == "__main__":
    quit_if_dir_exists(output_dir)
    mkdir(output_dir)
    create_binary_files()

