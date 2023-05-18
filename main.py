import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Always Visible Window")
root.geometry("400x300")

# Function to set the window as topmost
def top_True():
    button.config(text="Hide", bg="green", command=top_False)
    root.wm_attributes("-topmost", True)

# Function to unset the window as topmost
def top_False():
    button.config(text="Top", bg="gray", command=top_True)
    root.wm_attributes("-topmost", False)

# Function to clear the text in the Text widget
def clear_text():
    text.delete(1.0, tk.END)  

# Create the Top/Hide button
button = tk.Button(root, text="Top", width=10, height=2, bg="gray", fg="white", command=top_True)
button.place(x=302, y=5)

# Create the Clear button
clear_button = tk.Button(root, text="Clear", width=10, height=2, bg="gray", fg="white", command=clear_text)
clear_button.place(x=210, y=5)

# Create a font object with the desired font and size
font = Font(family="Roboto", size=16)

# Create a label with the desired text and font
label = tk.Label(root, text="Short Note", font=font)

# Place the label at coordinates (x=10, y=5) within the window
label.place(x=10, y=5)

# Create the Text widget
text = tk.Text(root, width=45, height=15)
text.place(x=20, y=50)

root.mainloop()
