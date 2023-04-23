# import tkinter as tk
# parent = tk.Tk()
# # create the widget.
# mytext = tk.Text(parent)
# # insert a string at the beginning
# mytext.insert('1.0', "-Python exercises, solution -")
# # insert a string into the current text
# mytext.insert('1.19', 'Practice,')
# # delete the first and last character (including a newline character)
# mytext.delete('1.0')
# mytext.delete('end - 2 chars')
# mytext.pack()
# parent.mainloop()

# import tkinter as tk
# from tkinter.ttk import Progressbar
# from tkinter import ttk
# parent = tk.Tk()
# parent.title("Progressbar")
# parent.geometry('350x200')
# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='green')
# bar = Progressbar(parent, length=220, style='black.Horizontal.TProgressbar')
# bar['value'] = 80
# bar.pack()
# parent.mainloop()

# import tkinter as tk
# parent = tk.Tk()
# parent.title("Radiobutton ")
# parent.geometry('350x200')
# radio1 = tk.Radiobutton(parent, text='First', value=1)
# radio2 = tk.Radiobutton(parent, text='Second', value=2)
# radio3 = tk.Radiobutton(parent, text='Third', value=3)
# radio1.pack()
# radio2.pack()
# radio3.pack()
# parent.mainloop()

import tkinter as tk
root = tk.Tk()
text_var = tk.DoubleVar()
spin_box = tk.Spinbox(
    root,
    from_=0.6,
    to=50.0,
    increment=.01,
    textvariable=text_var
)
spin_box.pack()
root.mainloop()
