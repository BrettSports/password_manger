from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    if len(website_text) == 0 or len(email_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="You didn't...", message="You didn't complete all the fields.")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_text} "
                                                            f"\nPassword: {pass_text} \nIs this okay?")
        if is_ok:
            with open("data.txt", "a") as my_file:
                my_file.write(f"{website_text} | {email_text} | {pass_text}\n")
                my_file.write("-" * 20 + "\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


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
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", command=add, width=35)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()