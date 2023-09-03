from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_label = Label(text="Website : ", pady=10)
website_label.grid(row=1, column=0, sticky="e")
# website entry
website_input = Entry(width=35, font=("", 13))
website_input.grid(row=1, column=1, columnspan=2, sticky="w")


# ---- email/username control field ----
# email label
email_label = Label(text="Email/Username : ", pady=10)
email_label.grid(row=2, column=0, sticky="e")
# email entry
email_input = Entry(width=35, font=("", 13))
email_input.grid(row=2, column=1, columnspan=2, sticky="w")


# ---- password control field ----
# password label
password_label = Label(text="Password : ", pady=10)
password_label.grid(row=3, column=0, sticky="e")
# password entry
password_input = Entry(width=21, font=("", 13))
password_input.grid(row=3, column=1, sticky="w")
# generate password button
gen_password_btn = Button(text="Generate Password", bg="#E7EFEC", fg="#183D3D", relief="groove")
gen_password_btn.grid(row=3, column=2, sticky="w")


# ---- add button field ----
Label(text="", pady=25).grid(row=4, column=0)  # empty label for vertical spacing
add_btn = Button(text="Add", width=31, bg="#337CCF", fg="white", font=("", 12, "bold"))
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
