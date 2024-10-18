import tkinter as tk


r = tk.Tk()
r.title('Continue')

button = tk.Button(r, text="Click", width=50, command=r.destroy)
button.pack(pady=20)


r.mainloop()
