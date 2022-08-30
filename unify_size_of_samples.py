from PIL import Image
from common import *

input_dir = "clean_hiragana"
output_dir = "unified_hiragana"

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
    
    bounding_box = find_bounding_box(image)
    
    sample = image.crop((bounding_box[0], bounding_box[2], bounding_box[1] + 1, bounding_box[3] + 1))
    
    sample_size_x = bounding_box[1] - bounding_box[0]
    sample_size_y = bounding_box[3] - bounding_box[2]
    
    if x_size - sample_size_x < y_size - sample_size_y:
        ratio = x_size / sample_size_x
    else:
        ratio = y_size / sample_size_y
    
    resized_sample = sample.resize((int(sample_size_x * ratio) - 2, int(sample_size_y * ratio) - 2), resample=Image.Resampling.NEAREST)
    
    sample_size_x = resized_sample.size[0]
    sample_size_y = resized_sample.size[1]
    
    centered_left = (x_size - sample_size_x) // 2
    centered_top = (y_size - sample_size_y) // 2
    
    unified_sample = Image.new('L', (image.size[0], image.size[1]), 0)
    unified_sample.paste(resized_sample, (centered_left,centered_top))
    
    return unified_sample

def unify_samples():
    for f in os.listdir(input_dir):
        if os.path.isfile(input_dir + "/" + f) and f.endswith(".png"):
            with Image.open(input_dir + "/" + f) as image:
                unify_sample(image).save(output_dir + "/" + f)

if __name__ == "__main__":
    quit_if_dir_exists(output_dir)
    mkdir(output_dir)
    unify_samples()

