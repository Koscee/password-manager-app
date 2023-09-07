from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

LABEL_PAD_Y = 8
LABEL_POS = "e"
CONTROL_PAD_X = 5
INPUT_FONT = ("", 13)
FILL_X = "ew"
BLUE_BG = "#337CCF"
BLUE_FG = "white"
GREEN_BG = "#E7EFEC"
GREEN_FG = "#183D3D"


def find_password():
    search_text = website_input.get().capitalize()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if search_text in data:
            found_record = data[search_text]
            email = found_record['email']
            password = found_record['password']
            messagebox.showinfo(title=search_text, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showwarning(title="Not Found", message=f"No details for {search_text} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    input_fields = (website_input, email_input, password_input)
    form_data = [input_field.get() for input_field in input_fields]
    (website, email, password) = form_data
    website = website.capitalize()

    new_record = {
        website: {
            "email": email,
            "password": password,
        }
    }

    for value in form_data:
        if not value:
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
            return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n   Email: {email}\n"
                                                          f"   Password: {password} \n\nIs it ok to save?")

    if is_ok:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)  # Read old data
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_record, data_file, indent=2)  # Write new data to file
        else:
            data.update(new_record)  # Update old data with new data
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=2)  # Write updated data to file
        finally:
            # clear all input fields except email
            for input_field in [field for field in input_fields if field != email_input]:
                input_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---- website control field ----
# website label
website_label = Label(text="Website : ")
website_label.grid(row=1, column=0, sticky=LABEL_POS, pady=LABEL_PAD_Y)
# website entry
website_input = Entry(font=INPUT_FONT)
website_input.focus()
website_input.grid(row=1, column=1, sticky=FILL_X, padx=CONTROL_PAD_X)
# search button
search_btn = Button(text="Search", bg=GREEN_BG, fg=GREEN_FG, relief="groove", command=find_password)
search_btn.grid(row=1, column=2, sticky=FILL_X, padx=CONTROL_PAD_X)

# ---- email/username control field ----
# email label
email_label = Label(text="Email/Username : ")
email_label.grid(row=2, column=0, sticky=LABEL_POS, pady=LABEL_PAD_Y)
# email entry
email_input = Entry(font=INPUT_FONT)
email_input.insert(0, "example@hotmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky=FILL_X, padx=CONTROL_PAD_X)

# ---- password control field ----
# password label
password_label = Label(text="Password : ")
password_label.grid(row=3, column=0, sticky=LABEL_POS, pady=LABEL_PAD_Y)
# password entry
password_input = Entry(font=INPUT_FONT)
password_input.grid(row=3, column=1, sticky=FILL_X, padx=CONTROL_PAD_X)
# generate password button
gen_password_btn = Button(text="Generate Password", bg=GREEN_BG, fg=GREEN_FG, relief="groove",
                          command=generate_password)
gen_password_btn.grid(row=3, column=2, sticky=FILL_X, padx=CONTROL_PAD_X)

# ---- add button field ----
Label(text="", pady=25).grid(row=4, column=0)  # empty label for vertical spacing
add_btn = Button(text="Add", bg=BLUE_BG, fg=BLUE_FG, font=("", 12, "bold"), command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky=FILL_X, padx=CONTROL_PAD_X)

window.mainloop()
