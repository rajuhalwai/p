import tkinter as tk

root = tk.Tk()

# Create a frame
frame = tk.Frame(root)
frame.pack()


buttonframe = tk.Frame(root)
buttonframe.pack(side="top")

# Create colored buttons
redbutton = tk.Button(frame, text='Red', fg='red')
redbutton.pack(side="left")

greenbutton = tk.Button(frame, text="Green", fg="green")
greenbutton.pack(side="left")

bluebutton = tk.Button(frame, text="Blue", fg="blue")
bluebutton.pack(side="bottom")

# Run the main loop
root.mainloop()
