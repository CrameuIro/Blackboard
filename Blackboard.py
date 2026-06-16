import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen",True)
root.configure(bg='black')
root.config(cursor='none')

root.bind("<Button-1>", lambda e:root.destroy())
root.bind("<Escape>", lambda e:root.destroy())

root.mainloop()