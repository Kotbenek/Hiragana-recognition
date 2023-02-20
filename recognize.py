import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageOps
import tensorflow as tf
import numpy as np
from common import *

old_x = None
old_y = None

IMAGE_SIZE = 64
CANVAS_SIZE = 256
LINE_SIZE = 4

MODEL_FILE = "model.h5"

INITIAL_TEXT = "Draw a hiragana character\nto recognize in the canvas"

def predict():
    # Invert image (black background, white character),
    # unify size of sample, turn it into normalized numpy array
    data = np.array(unify_sample(ImageOps.invert(image))) / 255

    data = data.reshape(-1, 64, 64, 1)
    pred = model.predict(data, verbose=0)[0]

    # Get top 5 predictions in terms of confidence
    ind = np.argpartition(pred, -5)[-5:]
    # Sort descending
    ind = np.flip(ind[np.argsort(pred[ind])])

    # Prediction text
    text = f"Prediction: {id_to_hiragana(ind[0])}\n"
    for r in ind:
        character = id_to_hiragana(int(r))
        conficence = f"{pred[int(r)] * 100:3.2f}".rjust(6)
        text += f"{character} ({conficence}%)\n"
    set_text(text)

def refresh_image():
    global img
    img = ImageTk.PhotoImage(image.resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.NEAREST))
    c.itemconfig("img", image=img)

def set_text(text):
    t.delete(1.0, tk.END)
    t.insert(tk.END, text)

def paint(event):
    global old_x, old_y, img

    # Use actual image coordinates
    event_x = event.x / CANVAS_SIZE * IMAGE_SIZE
    event_y = event.y / CANVAS_SIZE * IMAGE_SIZE

    # First point of a line - there is nothing to draw yet
    if old_x is None or old_y is None:
        old_x, old_y = event_x, event_y
        return

    draw.line([old_x, old_y, event_x, event_y], 0, width=LINE_SIZE)
    refresh_image()

    old_x = event_x
    old_y = event_y

    predict()

def mouse_button_released(event):
    global old_x, old_y
    old_x, old_y = None, None

def clear():
    draw.rectangle([0, 0, IMAGE_SIZE, IMAGE_SIZE], fill=255)
    refresh_image()
    set_text(INITIAL_TEXT)

if __name__ == '__main__':
    model = tf.keras.models.load_model(MODEL_FILE)

    root = tk.Tk()
    root.title("Hiragana recognition")

    image = Image.new("L", (IMAGE_SIZE, IMAGE_SIZE), 255)
    draw = ImageDraw.Draw(image)

    c = tk.Canvas(root, bg='white', width=CANVAS_SIZE, height=CANVAS_SIZE)

    img = ImageTk.PhotoImage(image)
    image_container = c.create_image(0, 0, anchor=tk.NW, image=img, tags="img")

    t = tk.Text(root, height=6, width=30)
    t.insert(tk.END, INITIAL_TEXT)

    b = tk.Button(root, text="CLEAR", command=clear)

    c.place(x=0, y=0)
    t.place(x=c.winfo_reqwidth(), y=0)
    b.place(x=c.winfo_reqwidth(), y=t.winfo_reqheight())

    c.bind('<B1-Motion>', paint)
    c.bind('<ButtonRelease-1>', mouse_button_released)

    root.geometry(f"{c.winfo_reqwidth() + t.winfo_reqwidth()}x{np.maximum(c.winfo_reqheight(), t.winfo_reqheight() + b.winfo_reqheight())}")

    root.resizable(False, False)

    root.mainloop()