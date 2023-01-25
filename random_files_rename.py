import tkinter as tk

window=tk.Tk()

btn=tk.Button(window, text="This is Button widget", fg='blue') # button
btn.place(x=80, y=100) # button position in the window

lbl=tk.Label(window, text="This is Label widget", fg='black', font=("Helvetica", 16))
lbl.place(x=60, y=50)

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()