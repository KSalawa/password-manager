from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="website:")
website_label.grid(column=0, row=1, sticky='e')
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="email/username:")
email_label.grid(column=0, row=2, sticky='e')
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="password:")
password_label.grid(column=0, row=3, sticky='e')
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="generate password")
generate_button.grid(column=2, row=3)

add_button = Button(text="add", width=36)
add_button.grid(column=1, row=4, columnspan=2)



mainloop()