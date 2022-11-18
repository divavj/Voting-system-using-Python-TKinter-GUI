from tkinter import *
import Image, ImageTk, ImageDraw

imgsize = (200,200)
canvas_bg = "#000000"

root = Tk()
## root.geometry("350x350")

panel = PanedWindow()
panel.pack(expand=0)

canvas = Canvas(panel, bg=canvas_bg)

blank_source = Image.new('RGBA',imgsize, "#ffffff")
blank = ImageTk.PhotoImage(blank_source)

label = Label(canvas, image=blank)
label.configure(image = blank)

canvas.pack( expand=0)
mainloop()