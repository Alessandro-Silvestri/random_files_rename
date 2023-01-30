import tkinter as tk
import random_rename_lib
renamer = random_rename_lib.Random_rename()
 
window=tk.Tk()
btn=tk.Button(window, text="   RENAME   ", fg='blue', command=renamer.rename_combined) # button
btn.place(x=100, y=100) # button position in the window

lbl=tk.Label(window, text="Renaming random jpg files", fg='black', font=("Helvetica", 12))
lbl.place(x=60, y=50)

window.title('Jpg Random Renamer')
window.geometry("300x200+1500+100") # size and position
window.mainloop()

