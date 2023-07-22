from tkinter import *
from tkinter import messagebox, simpledialog
from random import choice, randint, shuffle
import pyperclip
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                             f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def view_saved_passwords():
    master_password = "password" 
    entered_password = simpledialog.askstring("Master Password", "Enter the master password:", show='*')
    
    if entered_password == master_password:
        saved_passwords_window = Toplevel(window)
        saved_passwords_window.title("Saved Passwords")
        
        saved_passwords_text = Text(saved_passwords_window, width=80, height=10, font=("Helvetica", 12))
        saved_passwords_text.pack()

        try:
            with open("passwords.txt", "r") as data_file:
                saved_passwords_text.insert(END, data_file.read())
        except FileNotFoundError:
            messagebox.showinfo(title="File Not Found", message="No passwords.txt file found.")
    else:
        messagebox.showwarning("Access Denied", "Invalid master password.")

def update_password():
    website = website_entry.get()
    new_password = password_entry.get()

    if len(website) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have entered both website and password.")
    else:
        try:
            with open("passwords.txt", "r") as data_file:
                lines = data_file.readlines()
            
            with open("passwords.txt", "w") as data_file:
                for line in lines:
                    if website in line:
                        _, _, _ = line.split(" | ")
                        data_file.write(f"{website} | {email_entry.get()} | {new_password}\n")
                    else:
                        data_file.write(line)

            messagebox.showinfo(title="Success", message="Password updated successfully.")
        except FileNotFoundError:
            messagebox.showinfo(title="File Not Found", message="No passwords.txt file found.")

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg="#F0F0F0")

icon_path = resource_path("./assets/logo.ico")
window.iconbitmap(default=icon_path)

canvas = Canvas(height=200, width=200, bg="#F0F0F0", highlightthickness=0)
logo_img = PhotoImage(file=resource_path("assets/logo.png"))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="#F0F0F0", font=("Helvetica", 14, "bold"))
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="#F0F0F0", font=("Helvetica", 14, "bold"))
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="#F0F0F0", font=("Helvetica", 14, "bold"))
password_label.grid(row=3, column=0)

website_entry = Entry(width=35, font=("Helvetica", 12))
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35, font=("Helvetica", 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=10)
email_entry.insert(0, "Sharmaalok02gwl@gmail.com")
password_entry = Entry(width=21, font=("Helvetica", 12))
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=15, bg="#007BFF", fg="white", font=("Helvetica", 12, "bold"), command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Store Password", bg="#28A745", fg="white", font=("Helvetica", 12, "bold"), width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=8)
view_passwords_button = Button(text="View Saved Passwords", bg="#DC3545", fg="white", font=("Helvetica", 12, "bold"), width=36, command=view_saved_passwords)
view_passwords_button.grid(row=5, column=1, columnspan=2, pady=10)
update_password_button = Button(text="Update Password", bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"), width=36, command=update_password)
update_password_button.grid(row=6, column=1, columnspan=2)

window.mainloop()


