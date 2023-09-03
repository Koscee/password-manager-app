from tkinter import *

LABEL_PAD_Y = 10
INPUT_FONT = ("", 13)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    input_fields = [website_input, email_input, password_input]
    form_data = [input_field.get() for input_field in input_fields]
    separator = " | "
    record = separator.join(form_data)

    # write record to file
    with open("data.txt", mode="a") as data_file:
        data_file.write(f"{record}\n")

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
website_label = Label(text="Website : ", pady=LABEL_PAD_Y)
website_label.grid(row=1, column=0, sticky="e")
# website entry
website_input = Entry(width=35, font=INPUT_FONT)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="w")


# ---- email/username control field ----
# email label
email_label = Label(text="Email/Username : ", pady=LABEL_PAD_Y)
email_label.grid(row=2, column=0, sticky="e")
# email entry
email_input = Entry(width=35, font=INPUT_FONT)
email_input.insert(0, "example@hotmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="w")


# ---- password control field ----
# password label
password_label = Label(text="Password : ", pady=LABEL_PAD_Y)
password_label.grid(row=3, column=0, sticky="e")
# password entry
password_input = Entry(width=21, font=INPUT_FONT)
password_input.grid(row=3, column=1, sticky="w")
# generate password button
gen_password_btn = Button(text="Generate Password", bg="#E7EFEC", fg="#183D3D", relief="groove")
gen_password_btn.grid(row=3, column=2, sticky="w")


# ---- add button field ----
Label(text="", pady=25).grid(row=4, column=0)  # empty label for vertical spacing
add_btn = Button(text="Add", width=31, bg="#337CCF", fg="white", font=("", 12, "bold"), command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
