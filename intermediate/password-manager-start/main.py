import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            try:
                messagebox.showinfo(website, message=f"Email: {data[website]['email']}\n"
                                                     f"Password: {data[website]['password']} ")
            except KeyError:
                messagebox.showwarning(website, message=f"There is no such an Entry")
    except FileNotFoundError:
        messagebox.showwarning(website, message=f"No Data File Found")


def save():
    website = website_entry.get()
    username = username_entry.get()
    passwd = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": passwd,
        }
    }
    if len(website) == 0 or len(passwd) == 0:
        messagebox.showerror("Missing Field Error", message="Password or website can't be empty")
    else:
        messagebox.showinfo(f"{website}", message="Successfully Added!")

        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=2)
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=2)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=2)
        finally:
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            username_entry.insert(0, username)
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

pass_gen_window = tk.Tk()

pass_gen_window.title("Password Manager")
# pass_gen_window.minsize(width=500, height=500)
pass_gen_window.config(padx=50, pady=50)

pic = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="logo.png")
pic.create_image(100, 100, image=lock_image)
pic.grid(column=1, row=0)

# Website row
website_label = tk.Label(text="Website")
website_label.grid(column=0, row=2)

website_entry = tk.Entry(width=25)
website_entry.grid(column=1, row=2, columnspan=1)
website_entry.focus()

website_button = tk.Button(text="Search", command=search)
website_button.grid(column=2, row=2)
# Username row
username_label = tk.Label(text="Email/Username")
username_label.grid(column=0, row=3)

username_entry = tk.Entry(width=45)
username_entry.grid(column=1, row=3, columnspan=2)
username_entry.insert(0, "ahmed3ta@gmail.com")

# Password row
password_label = tk.Label(text="Password")
password_label.grid(column=0, row=4)

password_entry = tk.Entry(width=25)
password_entry.grid(column=1, row=4)
# password.entry.delete(0, END)
password_gen_button = tk.Button(text="Generate Password", command=generate_password)
password_gen_button.grid(column=2, row=4)

# Add to local filesystem
add_button = tk.Button(text="add", width=42, command=save)
add_button.grid(column=1, row=5, columnspan=2)

pass_gen_window.mainloop()
