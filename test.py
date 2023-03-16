import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('my window')

img = Image.open('285147919_693934881682873_3111502773218140248_n.jpg')
img2 = ImageTk.PhotoImage(img)


mycanvas = tk.Canvas(root, width=img.size[0], height=img.size[1])
mycanvas.pack()

mycanvas.create_image(0,0, anchor=tk.NW, image=img2)

root.mainloop()