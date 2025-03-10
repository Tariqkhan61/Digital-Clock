import tkinter as tk
from time import strftime

# make a root window. It will be an object
root = tk.Tk()

# now we set a Title jo k winsow k ooper dikhae day
root.title("Digital Clock")

# make a function which update time and date
def time():
    string = strftime('%H:%M:%S \n %d-%m-%Y')
    label.config(text=string)
    label.after(1000, time)  # is se hamara time function har second update hota rahega

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()
# use Main loop method.
root.mainloop()
