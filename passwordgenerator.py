
""" 
# Author: David Lepighe
#
# Description: 
#       This program help generate you passwords given the length wished by
#       the user. This can generate characters given by a sample the program 
#       and the password can be 6 to 15 characters long. 
"""
import random
from tkinter import *
from tkinter import messagebox

# Window management
app = Tk()
app.title("Password Generator")
app.geometry("300x100")
app.resizable(width= False, height= False) # Prevent the resizability

# Variables
sample = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#@$%&*(')"
password = ""
password_length = 0

# Function definitions
def generate_password():
    pass_len = character_entry.get() # Get the number from second entry 
    password = password_reveal.get() # Use the preset value (password) passed to 2nd entry
    
    # Handling errors
    if pass_len.isdigit() != True:
        messagebox.showerror("Digit Error", f"'{pass_len}' is not a digit.")
    elif int(pass_len) > 15:
        messagebox.showerror("Out of bound", f"{pass_len} is very large. Choose from 6 to 15")
    elif int(pass_len) < 6: 
        messagebox.showerror("Out of bound", f"{pass_len} is very small. Choose from 6 to 15.")
    elif pass_len == "":
        messagebox.showerror("No Entry", "Nothing was typed in the Entry")
    else:
        for i in range(int(pass_len)):
            character = random.choice(sample)
            password = password + str(character)
        
        # Return the password in the second entry
        password_reveal.insert(0, password)

def save_password():
    line = password_reveal.get() # Get from the second entry
    
    if line == "":
        print("Nothing in the entry")
        messagebox.showerror("Entry Empty", "Nothing is in the entry to save.")
    else:
        with open('saved_passwords.txt', 'a') as files:
            files.write(line + "\n")
        
        password_reveal.delete(0, END)
        messagebox.showinfo("Password saved", f"{line} was saved successfully!")

# GUI
message = Label(app, text= "Enter number of characters")
character_entry = Entry(app, textvariable= password_length)

message2 = Label(app, text= "Password Generated")
password_reveal = Entry(app, text= password)

generate_button = Button(app, text= "Generate", command= generate_password)
save_button = Button(app, text= "Save", command= save_password)

# Mainloop for the window
message.grid(row = 0, column= 0)
message2.grid(row = 1, column= 0)
character_entry.grid(row = 0, column= 1)
password_reveal.grid(row = 1, column= 1)
generate_button.place(x = 140, y = 60)
save_button.place(x = 220, y = 60, width= 55)
app.mainloop()