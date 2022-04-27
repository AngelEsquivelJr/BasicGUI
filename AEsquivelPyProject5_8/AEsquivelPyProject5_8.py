import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()

# app title
app.winfo_toplevel().title("Python GUI Project")

# object size
app.geometry("640x480")

# font style
fontstyle = tkFont.Font(family="Cooper", size =18)

labelExample = tk.Label(app, text="The system is idle.", font= fontstyle)


def SystemOn():
    labelExample.config(text ="System Running")

def SystemOff():
    labelExample.config(text ="System Off")



# virtual image
pixelVirtual = tk.PhotoImage(width=1, height=1)

labelExample.pack(side=tk.TOP)

# buttons
buttonExample1 = tk.Button(app, text="System On", image=pixelVirtual, width = 200, height =100, compound="c", command= SystemOn)
buttonExample1.place(x=100, y=400)

buttonExample2 = tk.Button(app, text="System Off", image=pixelVirtual, width = 200, height =100, compound="c", command= SystemOff)
buttonExample2.place(x=340, y=400)

# exit button
buttonExample3 = tk.Button(app, text="EXIT", command= app.quit)
buttonExample3.pack(side=tk.BOTTOM)
app.mainloop()
