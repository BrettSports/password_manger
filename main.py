from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for num in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for num in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(0, password)
    pass_entry.focus()
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_text = website_entry.get()
    email_text = email_entry.get()
    pass_text = pass_entry.get()
    new_data = {website_text: {
                "email": email_text,
                "password": pass_text
        }
    }

    if len(website_text) == 0 or len(email_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="You didn't...", message="You didn't complete all the fields.")
    else:
        try:
            with open("data.json", "r") as my_file:
                # Reading old data
                data = json.load(my_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as my_file:
                # Saving updated data
                json.dump(data, my_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


# -------------------------- SEARCH FUNCTION ----------------------------- #
def find_password():
    website_search = website_entry.get()
    email_search = email_entry.get()

    try:
        with open("data.json", "r") as my_file:
            data = json.load(my_file)
        if website_search in data:
            if data[website_search]["email"] == email_search:
                email = data[website_search]['email']
                password = data[website_search]['password']
                messagebox.showinfo(title="Match Found!", message=f"Website: {website_search} \nEmail: "
                                                                  f"{email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Match not found!", message="Email not found in data.")
        else:
            messagebox.showinfo(title="Match not found!", message="Website not found in data.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="Password manager not found!")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Brett Sports Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entry Fields
website_entry = Entry(width=41)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", command=add, width=30)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()